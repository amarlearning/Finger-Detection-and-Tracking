import cv2


def main():
    capture = cv2.VideoCapture(0)

    while True:
        ret, frame = capture.read()

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        edges_detec = cv2.Canny(gray_frame, 100, 200, apertureSize=3, L2gradient=True)

        cv2.imshow("Capture Frame", edges_detec)

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    capture.release()


if __name__ == '__main__':
    main()
