import cv2
import numpy as np

from colorfinder import ColorFinder


def distinct_locations(points, recurse=True):
    distinct_points = []
    # points = sorted( points, key=lambda el: (el[1], el[0]) )

    if recurse:
        points = sorted(points)
    else:
        points = sorted( points, key=lambda el: el[1] )

    # points = sorted(points, key=near_sort)
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

# def near_sort():

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


img_rgb = cv2.imread('snooker/3.png')
img_lab = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2LAB)
# cv2.imshow("rgb", img_rgb)
# cv2.imshow("lab", img_lab)
# cv2.waitKey(0)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('snooker/gray-pink-top.png', 0)
# template = cv2.imread('snooker/blue-top.png', 0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

threshold = 0.8
loc = np.where( res >= threshold )
points = distinct_locations( zip(*loc[::-1]) )

finder = ColorFinder()

for i, pt in enumerate(points):
    # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    w3 = int(w/4)
    pt0offset = pt[0] + 3
    pt1offset = pt[1] + 3

    rect = np.array([
        (pt0offset, pt1offset),
        (pt0offset + w3, pt1offset),
        (pt0offset + w3, pt1offset + h),
        (pt0offset, pt1offset + h)
    ])
    color = finder.find(img_rgb, rect)
    print("{:>2}. {}: {}".format(i+1, pt, color))
    cv2.drawContours(img_rgb, [rect], -1, (0, 255, 0), 1)

cv2.imshow('res-color-test.png', img_rgb)
cv2.waitKey(0)
# cv2.imwrite('res-color-test.png', img_rgb)
