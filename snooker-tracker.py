import cv2 as cv
import numpy as np

import locationhelper as loc

from balls import Balls
from colorfinder import ColorFinder


def main():
    img = load_image('1.png')
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    balls = mark_balls(img,
        get_balls_coords(img_gray),
        get_table_coords(img_gray))

    print(*balls.to_list(), sep='\n')

    cv.imshow('res-color-test.png', img)
    cv.waitKey(0)


def load_image(name, grayscale=False):
    iscolor = 0 if grayscale else 1
    return cv.imread('snooker/' + name, iscolor)


def mark_balls(image, balls_coords, table_coords):
    (w, h, points) = balls_coords
    balls = Balls()
    finder = ColorFinder()

    outline_table(image, table_coords)

    for i, pt in enumerate(points):
        rect = get_rectangle(pt, w, h)
        color = finder.find(image, rect)
        balls.add(*pt, color)

        cv.drawContours(image, [rect], -1, (0, 255, 0), 1)

    return balls


def get_balls_coords(image):
    (w, h, m1) = find_matches(image, 'blue-top-std2.png')
    (w, h, m2) = find_matches(image, 'pink-top-std2.png')

    matches = list(zip(*m1[::-1]))
    matches.extend( list(zip(*m2[::-1])) )

    return ( w, h, loc.distinct_locations(matches) )


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


def outline_table(image, table_coords):
    # print('tcoords:', table_coords)

    for corner, coords in table_coords.items():
        cv.circle(image, coords, 50, 255, 1)

    contour = np.array( sorted(list(table_coords.values())) )
    cv.drawContours(image, [contour], -1, (255, 255, 0), 1)

    return contour


def find_matches(image, template, threshold=0.8):
    template = load_image(template, grayscale=True)
    width, height = template.shape[::-1]
    matches = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)

    return (width, height, np.where( matches >= threshold ))


def get_rectangle(point, width, height):
    w4 = int(width/4)
    pt0offset = point[0] + 3
    pt1offset = point[1] + 3

    return np.array([
        (pt0offset, pt1offset),
        (pt0offset + w4, pt1offset),
        (pt0offset + w4, pt1offset + height),
        (pt0offset, pt1offset + height)
    ])


if __name__ == '__main__':
    main()
