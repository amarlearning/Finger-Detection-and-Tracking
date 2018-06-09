import cv2
import numpy as np


def main():
    
    # Blue Color Object Range
    # low = np.array([100, 70, 50])
    # high = np.array([140, 255, 255])

    # Green Color Object Range
    low = np.array([40, 50, 50])
    high = np.array([80, 255, 255])

    # Red Color Object Range
    # low = np.array([140, 150, 0])
    # high = np.array([180, 255, 255])

    windowOrignal = "Orignal Live Feed"
    windowMasked = "Masked Window Feed"
    windowColorObject = "Color Object Tracked"

    capture = cv2.VideoCapture(0)

    if capture.isOpened():
        flag, frameBGR = capture.read()
    else:
        flag = False

    while flag:

        flag, frameBGR = capture.read()

        frameHSV = cv2.cvtColor(frameBGR, cv2.COLOR_BGR2HSV)
        maskedFrame = cv2.inRange(frameHSV, low, high)
        BitwiseFrame = cv2.bitwise_and(frameBGR, frameBGR, mask=maskedFrame)

        cv2.imshow(windowColorObject, BitwiseFrame)
        cv2.imshow(windowMasked, maskedFrame)
        cv2.imshow(windowOrignal, frameBGR)

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    capture.release()


if __name__ == '__main__':
    main()
