import cv2 as cv
import numpy as np

import locationhelper as loc

from balls import Balls
from colorfinder import ColorFinder


def main():
    img = load_image('1.png')
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    table_contour = outline_table( img, get_table_coords(img_gray) )
    img_corrected = correct_perspective(img, table_contour)
    img_gray = cv.cvtColor(img_corrected, cv.COLOR_BGR2GRAY)

    balls = mark_balls(img_corrected,
        get_balls_coords(img_gray),
        table_contour)

    print(*balls.to_list(), sep='\n')

    cv.imshow('res-color-test.png', img_corrected)
    # cv.imwrite('corrected-perspective-gray.png', img_gray)
    cv.waitKey(0)


def load_image(name, grayscale=False):
    iscolor = 0 if grayscale else 1
    return cv.imread('snooker/' + name, iscolor)


def mark_balls(image, balls_coords, table_contour):
    (w, h, points) = balls_coords
    balls = Balls()
    finder = ColorFinder()

    for i, pt in enumerate(points):
        # if is_outside_table(pt, table_contour):
        #     continue

        rect = get_rectangle(pt, w, h)
        color = finder.find(image, rect)

        if color != "cloth_green":
            balls.add(*pt, color)
            cv.drawContours(image, [rect], -1, (0, 255, 0), 1)

    return balls


def get_balls_coords(image):
    (w, h, m1) = find_matches(image, 'pink-top-prog-gray-corrected.png')
    (w, h, m2) = find_matches(image, 'blue-top-prog-gray-corrected.png')
    (w, h, m3) = find_matches(image, 'red-top-prog-gray-corrected.png')
    # (w, h, m1) = find_matches(image, 'pink-top-corrected.png')
    # (w, h, m2) = find_matches(image, 'pink-top-corrected.png')

    matches = list(zip(*m1[::-1]))
    matches.extend( list(zip(*m2[::-1])) )
    matches.extend( list(zip(*m3[::-1])) )

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


def is_outside_table(point, contour):
    return cv.pointPolygonTest(contour, point, False) < 0


def find_matches(image, template, threshold=0.8):
    template = load_image(template, grayscale=True)
    width, height = template.shape[::-1]
    matches = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)

    return (width, height, np.where( matches >= threshold ))


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

    h, status = cv.findHomography( coords, plane )

    return cv.warpPerspective( image, h, size )

    # cv.imshow('Corrected perspective', img_corrected)
    # cv.imwrite('corrected-perspective.png', img_corrected)
    # cv.waitKey(0)


if __name__ == '__main__':
    main()
