import cv2


def passFunction(x):
    pass


def main():
    windowname = "OpenCV Media Player"
    cv2.namedWindow(windowname)

    videoFilePath = "/media/amarpandey/Media Files/Movies/Game Of Thrones/Season Seven/Game.of.Thrones.S07E03.720p.WEB.h264-TBS[eztv].mkv"

    capture = cv2.VideoCapture(videoFilePath)
    cv2.createTrackbar('FrameSpeed', windowname, 10, 600, passFunction)

    while (capture.isOpened()):

        FrameSpeed = cv2.getTrackbarPos('FrameSpeed', windowname)
        flag, frame = capture.read()

        if FrameSpeed <= 0: FrameSpeed = 1

        if flag:
            cv2.imshow(windowname, frame)
            if cv2.waitKey(FrameSpeed) & 0xFF == 27:  # because 33 * FPS == 1 second
                break
        else:
            break

    cv2.destroyWindow(windowname)
    capture.release()


if __name__ == '__main__':
    main()
