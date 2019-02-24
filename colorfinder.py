from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np
import cv2

class ColorFinder:
    def __init__(self):
        # initialize the colors dictionary, containing the color
        # name as the key and the RGB tuple as the value
        # colors = OrderedDict({
        #     "red": (255, 0, 0),
        #     "green": (0, 255, 0),
        #     "blue": (0, 0, 255),
        #     "pink": (255, 150, 150),
        #     "brown": (150, 90, 20),
        #     "yellow": (0, 255, 255),
        #     "white": (255, 255, 255),
        #     "black": (0, 0, 0)
        # })
        colors = OrderedDict({
            "red": (155, 0, 0),
            "green": (0, 100, 50),
            "blue": (0, 100, 200),
            "pink": (255, 150, 150),
            "brown": (150, 90, 20),
            "yellow": (0, 255, 255),
            "white": (255, 255, 200),
            "black": (0, 0, 0)
        })
        # allocate memory for the L*a*b* image, then initialize
        # the color names list
        self.lab = np.zeros((len(colors), 1, 3), dtype="uint8")
        self.colorNames = []
        self.ii = 0

        # loop over the colors dictionary
        for (i, (name, rgb)) in enumerate(colors.items()):
            # update the L*a*b* array and the color names list
            self.lab[i] = rgb
            self.colorNames.append(name)

        # convert the L*a*b* array from the RGB color space
        # to L*a*b*
        # self.lab = cv2.cvtColor(self.lab, cv2.COLOR_RGB2LAB)

    def find(self, image, c):
        # construct a mask for the contour, then compute the
        # average L*a*b* value for the masked region
        mask = np.zeros(image.shape[:2], dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)
        mask = cv2.erode(mask, None, iterations=2)
        mean = cv2.mean(image, mask=mask)[:3]

        # cv2.imwrite('colors/res-color-test-img-{}.png'.format(self.ii), image)
        # cv2.imwrite('colors/res-color-test-mask-{}.png'.format(self.ii), mask)
        # self.ii += 1
        # cv2.imshow("Mask", mask)
        # cv2.waitKey(0)

        # initialize the minimum distance found thus far
        minDist = (np.inf, None)

        # loop over the known L*a*b* color values
        for (i, row) in enumerate(self.lab):
            # compute the distance between the current L*a*b*
            # color value and the mean of the image
            d = dist.euclidean(row[0][::-1], mean)
            # print('mean is:', mean, 'd is:', d)

            # if the distance is smaller than the current distance,
            # then update the bookkeeping variable
            if d < minDist[0]:
                minDist = (d, i)

        # return the name of the color with the smallest distance
        # print('minDist:', minDist)
        return self.colorNames[minDist[1]]
