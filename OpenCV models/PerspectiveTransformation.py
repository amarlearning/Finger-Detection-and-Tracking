import cv2
import numpy as np

countClicks = 0
coordinates = np.float32([])

windowname = "Sample Image"
imagePath = "../data/dummy-new.jpeg"

image = cv2.imread(imagePath)
copyimage = image.copy()

cv2.namedWindow(windowname, cv2.WINDOW_NORMAL)


def captures(event, x, y, flags, params):
    global countClicks, coordinates, image

    if countClicks < 4:
        if event == cv2.EVENT_LBUTTONDBLCLK:
            countClicks = countClicks + 1
            coordinates = np.append(coordinates, np.float32([x, y]), axis=0)
            cv2.circle(image, (x, y), 5, (0, 0, 255), -1)


cv2.setMouseCallback(windowname, captures)


def main():
    global countClicks, coordinates, copyimage

    cv2.resizeWindow(windowname, 700, 700)

    while (countClicks < 4):
        preseedKey = cv2.waitKey(1)
        cv2.imshow(windowname, image)

        if preseedKey & 0xFF == 27:
            break

    pointone = np.float32(
        [[coordinates[0], coordinates[1]],
         [coordinates[2], coordinates[3]],
         [coordinates[4], coordinates[5]],
         [coordinates[6], coordinates[7]]])
    pointtwo = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

    perspective = cv2.getPerspectiveTransform(pointone, pointtwo)
    output = cv2.warpPerspective(copyimage, perspective, (310, 310))

    cv2.imshow("Output Image", output)
    cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
