import argparse
import json
import cv2 as cv
import numpy as np

import locationhelper as loc

from ball import Ball
from balls import Balls
from colorfinder import ColorFinder


def main(args):
    img_corrected = find_table_and_correct_perspective( args['filename'] )
    img_gray = cv.cvtColor(img_corrected, cv.COLOR_BGR2GRAY)

    balls = mark_balls(img_corrected,
        get_balls_coords(img_gray))

    if 'svg' in args['show']:
        print_svg(balls)
    if 'json' in args['show']:
        json = print_json(1, 1, balls)
    if 'list' in args['show']:
        print(*balls.to_list(), sep='\n')
    if 'image' in args['show']:
        show_image(img_corrected)

    return json


def load_image(name, grayscale=False):
    iscolor = 0 if grayscale else 1
    return cv.imread('snooker/' + name, iscolor)


def find_table_and_correct_perspective(img_path):
    img = load_image(img_path)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    table_contour = outline_table( get_table_coords(img_gray) )

    return correct_perspective(img, table_contour)


def mark_balls(image, balls_coords):
    w, h, points = balls_coords
    balls = Balls()
    finder = ColorFinder()

    for i, pt in enumerate(points):
        rect = get_rectangle(pt, w, h)
        color = finder.find(image, rect)

        if color != "cloth_green":
            balls.add(*pt, color)
            cv.drawContours(image, [rect], -1, (0, 255, 0), 1)

    return balls


def get_balls_coords(image):
    # TODO parallel
    w, h, m1 = find_matches(image, 'pink-top-prog-gray-corrected.png')
    w, h, m2 = find_matches(image, 'blue-top-prog-gray-corrected.png')
    w, h, m3 = find_matches(image, 'red-top-prog-gray-corrected.png')

    matches = list(zip(*m1[::-1]))
    matches.extend( list(zip(*m2[::-1])) )
    matches.extend( list(zip(*m3[::-1])) )

    return w, h, loc.distinct_locations(matches)


def get_table_coords(image):
    coords = {}
    corners = ["top_left", "top_right", "bottom_left", "bottom_right"]

    for corner in corners:
        template = load_image('pocket-{}.png'.format(corner), grayscale=True)
        w, h = template.shape[::-1]

        match = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)

        _, _, _, top_left = cv.minMaxLoc(match)
        center = (top_left[0] + int(w/2), top_left[1] + int(h/2))

        coords[corner] = center

    return coords


def outline_table(table_coords):
    return np.array( sorted(list(table_coords.values())) )


def find_matches(image, template, threshold=0.8):
    template = load_image(template, grayscale=True)
    width, height = template.shape[::-1]
    matches = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)

    return width, height, np.where( matches >= threshold )


def get_rectangle(point, width, height):
    w4 = int(width/4)
    h2 = int(height/2)
    pt0offset = point[0] + 3
    pt1offset = point[1] + 5

    return np.array([
        (pt0offset, pt1offset),
        (pt0offset + w4, pt1offset),
        (pt0offset + w4, pt1offset + h2),
        (pt0offset, pt1offset + h2)
    ])


def correct_perspective(image, coords):
    size = (758, 1440)
    plane = np.array([
        [0, size[1]-1],
        [0, 0],
        [size[0]-1, 0],
        [size[0]-1, size[1]-1]
    ])

    h, _ = cv.findHomography( coords, plane )

    return cv.warpPerspective( image, h, size )


def show_image(image, title='Result image'):
    cv.imshow(title, image)
    # cv.imwrite('corrected-perspective-gray.png', image)
    cv.waitKey(0)


def print_svg(balls):
    for ball in map( translate_coords, balls.to_list() ):
        print('<use xlink:href="#ball" x="{x}" y="{y}" fill="{fill}"/>'.format(
            x=ball.x, y=ball.y, fill=ball.color))


def print_json(game_id, timestamp, balls):
    return json.dumps(
        {
            'game_id': game_id,
            'timestamp': timestamp,
            'balls': list(map( raw_ball, balls.to_list() ))
        }
    )


def raw_ball(ball):
    return vars( translate_coords(ball) )


def translate_coords(ball):

    # cushion = 28px; template/position offset = 8px
    x = ball.x + 10 - 28
    x_coeff = x / (758 - 2*28)

    if x_coeff == 0.5:
        x = 0
    elif x_coeff < 0.5:
        x_coeff = 0.5 - x_coeff
        x = 33.867 * x_coeff * 2
        # x = 33.867 - x
    else:
        x_coeff = 1 - x_coeff
        x = 33.867 * x_coeff * 2
        x = -33.867 + x

    # cushion = 48px; template/position offset = 45px
    y = ball.y + 65 - 28
    y_coeff = y / (1440 - 28)
    y = (143.962) * y_coeff
    y = (143.962) - y

    return Ball(x, y, ball.color)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('--show', nargs='+')
    args = vars(parser.parse_args())

    if args['show']:
        show = {}

        for elem in args['show']:
            show[elem] = True

        args['show'] = show
    else:
        args['show'] = {}


    main(args)
