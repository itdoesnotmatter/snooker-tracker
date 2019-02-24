import cv2 as cv
import numpy as np

from balls import Balls
from colorfinder import ColorFinder


img_rgb = cv.imread('snooker/3.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('snooker/gray-pink-top.png', 0)
# template = cv.imread('snooker/blue-top.png', 0)

w, h = template.shape[::-1]

res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)

threshold = 0.8
loc = np.where( res >= threshold )

balls = Balls( zip(*loc[::-1]) )
points = balls.locations

finder = ColorFinder()

for i, pt in enumerate(points):
    w4 = int(w/4)
    pt0offset = pt[0] + 3
    pt1offset = pt[1] + 3

    rect = np.array([
        (pt0offset, pt1offset),
        (pt0offset + w4, pt1offset),
        (pt0offset + w4, pt1offset + h),
        (pt0offset, pt1offset + h)
    ])
    color = finder.find(img_rgb, rect)
    cv.drawContours(img_rgb, [rect], -1, (0, 255, 0), 1)
    balls.add(*pt, color)

print(*balls.to_list(), sep='\n')

cv.imshow('res-color-test.png', img_rgb)
cv.waitKey(0)
