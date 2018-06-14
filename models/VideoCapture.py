import cv2


def main():
    framerate = 30
    resolution = (640, 480)
    window_name = "Live Video Feed"
    videoCapturePath = "../Output/Output.avi"

    cv2.namedWindow(window_name)
    capture = cv2.VideoCapture(0)

    codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')

    videoCapture = cv2.VideoWriter(videoCapturePath, codec, framerate, resolution)

    if capture.isOpened():
        flag, frame = capture.read()
    else:
        flag = False

    while flag:

        flag, frame = capture.read()
        videoCapture.write(frame)
        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyWindow(window_name)
    videoCapture.release()
    capture.release()


if __name__ == '__main__':
    main()
