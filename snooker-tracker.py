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


img = load_image('1.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

(w, h, m1) = find_matches(img_gray, 'blue-top-std2.png')
(w, h, m2) = find_matches(img_gray, 'pink-top-std2.png')

matches = list(zip(*m1[::-1]))
matches.extend( list(zip(*m2[::-1])) )

points = loc.distinct_locations( matches )
finder = ColorFinder()
balls = Balls()

for i, pt in enumerate(points):
    rect = get_rectangle(pt, w, h)
    color = finder.find(img, rect)
    balls.add(*pt, color)

    cv.drawContours(img, [rect], -1, (0, 255, 0), 1)


print(*balls.to_list(), sep='\n')

cv.imshow('res-color-test.png', img)
cv.waitKey(0)
