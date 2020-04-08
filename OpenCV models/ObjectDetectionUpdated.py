import cv2
import numpy as np
from collections import deque

def rescale_frame(frame, wpercent=130, hpercent=130):
    width = int(frame.shape[1] * wpercent / 100)
    height = int(frame.shape[0] * hpercent / 100)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

def main():

    buffer_size = 64

    # Blue Color Object Range
    blue_low = np.array([110, 100, 100])
    blue_high = np.array([130, 255, 255])

    # Green Color Object Range
    green_low = np.array([50, 100, 100])
    green_high = np.array([70, 255, 255])

    # Red Color Object Range
    red_low = np.array([0, 100, 100])
    red_high = np.array([10, 255, 255])

    windowOrignal = "Orignal Live Feed"
    windowMasked = "Masked Window Feed"
    windowColorObject = "Color Object Tracked"

    pts = deque(maxlen=buffer_size)
    capture = cv2.VideoCapture(0)

    if capture.isOpened():
        flag, frame_bgr = capture.read()
    else:
        flag = False

    while flag:

        center = None
        flag, frame_bgr = capture.read()
        frame_bgr = cv2.flip(frame_bgr, 1)

        blurred = cv2.GaussianBlur(frame_bgr, (11, 11), 0)
        frame_hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(frame_hsv, blue_low, blue_high)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        image, contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:

            c = max(contours, key=cv2.contourArea)

            moment = cv2.moments(c)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            center = (int(moment["m10"] / moment["m00"]), int(moment["m01"] / moment["m00"]))

            if radius > 0.5:
                cv2.circle(frame_bgr, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(frame_bgr, center, 5, (0, 0, 255), -1)

        pts.append(center)

        for i in range(1, len(pts)):
            if pts[i - 1] is None or pts[i] is None:
                continue
            thickness = int(np.sqrt(buffer_size / float(buffer_size - i + 1)) * 2.5)
            cv2.line(frame_bgr, pts[i - 1], pts[i], (0, 0, 255), thickness)

        cv2.imshow(windowOrignal, rescale_frame(frame_bgr))

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()
    capture.release()

if __name__ == '__main__':
    main()