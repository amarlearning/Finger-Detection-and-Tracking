import cv2
import numpy as  np


def main():
    kernal = np.ones((5, 5), np.uint8)
    image = cv2.imread("../data/contour_sample.jpg", 1)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, binay_thresh = cv2.threshold(gray_image, 90, 255, cv2.THRESH_BINARY)
    cv2.imshow("Binary Thresholding Image", binay_thresh)

    '''
    erode = cv2.erode(binay_thresh, kernal, iterations=1)
    cv2.imshow("Eroded Image", erode)
    '''

    image_two, contours, hierarchy = cv2.findContours(binay_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, 55, (0, 255, 0), 3)

    cv2.imshow("Contoured Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
