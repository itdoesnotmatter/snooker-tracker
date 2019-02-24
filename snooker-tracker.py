import cv2 as cv
import numpy as np

from colorfinder import ColorFinder


def distinct_locations(points, recurse=True):
    distinct_points = []

    if recurse:
        points = sorted(points)
    else:
        points = sorted( points, key=lambda el: el[1] )

    near_points = []
    prev_p = points[0]

    for p in points:
        if near(p, prev_p):
            near_points.append(p)
        else:
            if len(near_points) == 1:
                near_points.append(prev_prev_p)
            new_point = points_avg(near_points) if near_points else prev_p
            distinct_points.append( new_point )
            near_points = []
        prev_prev_p = prev_p
        prev_p = p

    if near_points:
        distinct_points.append( points_avg(near_points) )
    else:
        distinct_points.append( prev_p )

    return remove_dupes(distinct_points) if recurse else distinct_points


def remove_dupes(points):
    unduped_points, near_points = [], []
    prev_p = points[0]

    for p in points:

        if in_threshold( p[0], prev_p[0] ):
            near_points.append(p)
        else:
            if len(near_points) > 0:
                if len(near_points) == 1:
                    near_points.append(prev_prev_p)
                near_points = distinct_locations( near_points, False )
            elif len(near_points) == 0:
                near_points.append(prev_p)

            unduped_points.extend( near_points )
            near_points = []

        prev_prev_p = prev_p
        prev_p = p

    if len(near_points) > 0:
        unduped_points.extend( distinct_locations(near_points, False) )
    else:
        unduped_points.append(prev_p)

    return unduped_points


def near(p1, p2):
    return in_threshold( p1[0], p2[0] ) \
        and in_threshold( p1[1], p2[1] )


def in_threshold(n1, n2, threshold=5):
    return abs(n1 - n2) < threshold


def avg(nums):
    return int( sum(nums) / len(nums) )


def points_avg(points):
    p0s = list(p[0] for p in points)
    p1s = list(p[1] for p in points)

    return ( avg(p0s), avg(p1s))


img_rgb = cv.imread('snooker/3.png')
img_lab = cv.cvtColor(img_rgb, cv.COLOR_BGR2LAB)
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('snooker/gray-pink-top.png', 0)
# template = cv.imread('snooker/blue-top.png', 0)

w, h = template.shape[::-1]

res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)

threshold = 0.8
loc = np.where( res >= threshold )
points = distinct_locations( zip(*loc[::-1]) )

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
    print("{:>2}. {}: {}".format(i+1, pt, color))
    cv.drawContours(img_rgb, [rect], -1, (0, 255, 0), 1)

cv.imshow('res-color-test.png', img_rgb)
cv.waitKey(0)
