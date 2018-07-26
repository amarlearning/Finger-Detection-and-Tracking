import cv2
import numpy as np


def main():
    kernal = np.ones((5, 5), np.uint8)

    image = cv2.imread("../data/4.2.05.tiff", 1)

    blurimage = cv2.GaussianBlur(image, (15, 15), 0)

    dialate = cv2.dilate(image, kernal, iterations=1)
    erosion = cv2.erode(image, kernal, iterations=1)

    cv2.imshow("Dialated Image", dialate)
    cv2.imshow("Eroded Image", erosion)
    cv2.imshow("Blur Image", blurimage)
    cv2.imshow("Orignal Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
