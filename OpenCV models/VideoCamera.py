import cv2


def main():
    window_name = "Live Video Feed"
    cv2.namedWindow(window_name)

    capture = cv2.VideoCapture(0)

    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    if capture.isOpened():
        flag, frame = capture.read()
    else:
        flag = False

    while flag:

        flag, frame = capture.read()

        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyWindow(window_name)
    capture.release()


if __name__ == '__main__':
    main()
