import cv2
import numpy as np


def main():
    const = 1
    max_value = 255
    faces_image = cv2.imread("../data/faces.jpeg", 1)

    faces_image = cv2.cvtColor(faces_image, cv2.COLOR_BGR2HSV)
    faces_image_700 = cv2.resize(faces_image, (700, 700))

    hue = faces_image_700[:, :, 0]
    satr = faces_image_700[:, :, 1]
    value = faces_image_700[:, :, 2]

    hsv_images = np.concatenate((hue, satr, value), axis=1)

    _, hue_thresh = cv2.threshold(hue, 10, max_value, cv2.THRESH_BINARY_INV)
    _, satr_thresh = cv2.threshold(satr, 40, max_value, cv2.THRESH_BINARY)

    skin_image = cv2.bitwise_and(hue_thresh, satr_thresh)

    cv2.imshow("Hue Image", hue_thresh)
    cv2.imshow("Saturation Image", satr_thresh)

    cv2.imshow("SKin Detected Image", skin_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
