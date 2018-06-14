import time

import cv2


def main():
    angle = 0
    scale = 0.1
    windowName = "Video Rotation"
    cv2.namedWindow(windowName, cv2.WINDOW_FULLSCREEN)

    capture = cv2.VideoCapture(0)

    if capture.isOpened():
        flag, frame = capture.read()
    else:
        flag = False

    rows, cols, channels = frame.shape

    while flag:

        if angle > 360:
            angle = 0

        if scale < 2:
            scale = scale + 0.1
        else:
            scale = 0.1

        flag, frame = capture.read()

        rotationmatrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, scale)
        transformedoutput = cv2.warpAffine(frame, rotationmatrix, (cols, rows))

        cv2.imshow(windowName, transformedoutput)

        angle = angle + 1
        time.sleep(0.01)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()
    capture.release()


if __name__ == '__main__':
    main()
