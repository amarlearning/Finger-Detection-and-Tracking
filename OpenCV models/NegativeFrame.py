import cv2


def main():
    capture = cv2.VideoCapture(0)

    if capture.isOpened():
        flag, frame = capture.read()
    else:
        flag = False

    while flag:

        flag, frame = capture.read()

        frame = abs(255 - frame)

        cv2.imshow("Video Camera", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
