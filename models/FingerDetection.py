import cv2
import numpy as np


def rescale_frame(frame, wpercent=100, hpercent=100):
    width = int(frame.shape[1] * wpercent / 100)
    height = int(frame.shape[0] * hpercent / 100)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)


def draw_rect(frame):
    rows, cols, _ = frame.shape

    hand_rect_one_x = np.array(
        [6 * rows / 20, 6 * rows / 20, 6 * rows / 20, 9 * rows / 20, 9 * rows / 20, 9 * rows / 20, 12 * rows / 20,
         12 * rows / 20, 12 * rows / 20], dtype=np.uint32)

    hand_rect_one_y = np.array(
        [9 * cols / 20, 10 * cols / 20, 11 * cols / 20, 9 * cols / 20, 10 * cols / 20, 11 * cols / 20, 9 * cols / 20,
         10 * cols / 20, 11 * cols / 20], dtype=np.uint32)

    hand_rect_two_x = hand_rect_one_x + 20
    hand_rect_two_y = hand_rect_one_y + 20

    for i in range(hand_rect_one_x.size):
        cv2.rectangle(frame, (hand_rect_one_y[i], hand_rect_one_x[i]),
                      (hand_rect_two_y[i], hand_rect_two_x[i]),
                      (0, 255, 0), 2)

    black_frame = np.zeros(frame.shape, dtype=frame.dtype)
    return np.vstack([frame, black_frame])


def main():
    capture = cv2.VideoCapture(0)

    while capture.isOpened():
        _, frame = capture.read()

        frame = rescale_frame(frame)
        frame = draw_rect(frame)

        cv2.imshow("Live Feed", frame)

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    capture.release()


if __name__ == '__main__':
    main()
