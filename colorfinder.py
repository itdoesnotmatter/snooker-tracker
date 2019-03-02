from scipy.spatial import distance as dist
from collections import OrderedDict

import numpy as np
import cv2 as cv


class ColorFinder:
    def __init__(self):
        colors = OrderedDict({
            "cloth_green": (0, 100, 0),
            "white": (255, 255, 200),
            "red": (155, 50, 10),
            "yellow": (255, 255, 0),
            "green": (0, 100, 50),
            "brown": (140, 100, 20),
            "blue": (0, 100, 200),
            "pink": (255, 150, 150),
            "black": (0, 0, 0)
        })
        self.colors = np.zeros((len(colors), 1, 3), dtype="uint8")
        self.colorNames = []

        for (i, (name, rgb)) in enumerate(colors.items()):
            self.colors[i] = rgb
            self.colorNames.append(name)


    def find(self, image, contour):
        mask = np.zeros(image.shape[:2], dtype="uint8")
        cv.drawContours(mask, [contour], -1, 255, -1)
        mask = cv.erode(mask, None, iterations=2)
        mean = cv.mean(image, mask=mask)[:3]

        minDist = (np.inf, None)

        for (i, row) in enumerate(self.colors):
            d = dist.euclidean(row[0][::-1], mean)

            if d < minDist[0]:
                minDist = (d, i)

        return self.colorNames[ minDist[1] ]
