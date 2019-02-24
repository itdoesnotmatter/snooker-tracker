import cv2 as cv
import numpy as np

import locationhelper as loc

from balls import Balls
from colorfinder import ColorFinder


def load_image(name, grayscale=False):
    iscolor = 0 if grayscale else 1
    return cv.imread('snooker/' + name, iscolor)


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


def get_balls_coords(image):
    img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    (w, h, m1) = find_matches(img_gray, 'blue-top-std2.png')
    (w, h, m2) = find_matches(img_gray, 'pink-top-std2.png')

    matches = list(zip(*m1[::-1]))
    matches.extend( list(zip(*m2[::-1])) )

    return ( w, h, loc.distinct_locations(matches) )


def mark_balls(image, balls_coords):
    (w, h, points) = balls_coords
    balls = Balls()
    finder = ColorFinder()

    for i, pt in enumerate(points):
        rect = get_rectangle(pt, w, h)
        color = finder.find(image, rect)
        balls.add(*pt, color)

        cv.drawContours(image, [rect], -1, (0, 255, 0), 1)

    return balls


def get_table_coords():
    # top_left = 
    return {
        "top_left": 0,
        "top_right": 0,
        "bottom_left": 0,
        "bottom_right": 0
    }


img = load_image('1.png')
balls = mark_balls(img, get_balls_coords(img))

print(*balls.to_list(), sep='\n')

cv.imshow('res-color-test.png', img)
cv.waitKey(0)
