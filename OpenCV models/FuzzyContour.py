import random

import cv2
import numpy as np


def main():
    kernal = np.ones((5, 5), np.uint8)
    image = cv2.imread("../data/fuzzy.png", 1)

    # converting the image into gray scale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # threshold the image to diff object for background
    _, thresh = cv2.threshold(gray_image, 50, 255, cv2.THRESH_BINARY_INV)

    # dilating the image to remove noise from objects
    dilated_image = cv2.dilate(thresh, kernal, iterations=2)

    # finding all contours in fuzzy image
    _, contours, _ = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # new image to draw contour objects
    sample = np.zeros((image.shape[0], image.shape[1], 3), np.uint8)

    for cnt in contours:

        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # get contour area using 'contourArea' method
        area_cnt = cv2.contourArea(cnt)

        # get the perimeter of any contour using 'arcLength'
        perimeter_cnt = cv2.arcLength(cnt, True)

        if int(area_cnt) > 1000:
            cv2.drawContours(sample, [cnt], -1, color, -1)

        print("Area : {}, Perimeter : {}".format(area_cnt, perimeter_cnt))

    cv2.imshow("Contoured Image", sample)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
