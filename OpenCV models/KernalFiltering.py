import cv2
import numpy as np


def main():
    image = cv2.imread("../data/7.1.01.tiff", 1)

    '''
    # Kernal or Convolution matrix for Identity Filter

    kernal = np.array(([0, 0, 0],
                       [0, 1, 0],
                       [0, 0, 0]), np.float32)

    # Kernal or Convolution matrix for Edge Detection

    kernal = np.array(([-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]), np.float32)

    '''

    # Kernal or Convolution matrix for Box BLue Filter

    kernal = np.ones((5, 5), np.uint8) / 25
    output = cv2.filter2D(image, -1, kernal)

    # Low pass filters implementation
    box_blur = cv2.boxFilter(image, -1, (31, 31))
    simple_blur = cv2.blur(image, (21, 21))
    gaussian_blur = cv2.GaussianBlur(image, (51, 51), 0)

    cv2.imshow("Orignal Image", image)
    cv2.imshow("Filtered Image", output)

    cv2.imshow("Box Blur", box_blur)
    cv2.imshow("Simple Blur", simple_blur)
    cv2.imshow("Gaussian Blur", gaussian_blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
