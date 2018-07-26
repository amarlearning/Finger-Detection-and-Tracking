import cv2
import numpy as np


def main():
    capture = cv2.VideoCapture(0)

    while True:
        ret, frame = capture.read()

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        edges_detec = cv2.Canny(gray_frame, 50, 250, apertureSize=5, L2gradient=True)

        hough_lines = cv2.HoughLines(edges_detec, 1, np.pi / 180, 200)

        if hough_lines is not None:
            for rho, theta in hough_lines[0]:
                x0 = rho * np.cos(theta)
                y0 = rho * np.sin(theta)

                ptsX = (int(x0 + 1000 * (-np.sin(theta))), int(y0 + 1000 * (np.cos(theta))))
                ptsY = (int(x0 - 1000 * (-np.sin(theta))), int(y0 - 1000 * (np.cos(theta))))
                cv2.line(frame, ptsX, ptsY, (0, 255, 0), 2)

        cv2.imshow("Capture Frame", frame)

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    capture.release()


if __name__ == '__main__':
    main()
