import cv2


def passFunction(x):
    pass

def main():

    windowName = "Transition Effect"
    basePath = "/home/amarpandey/PycharmProjects/OpenCV/data/"

    imageOneName = basePath + "lena_color_512.tif"
    imageTwoName = basePath + "mandril_color.tif"

    cv2.namedWindow("Transition Effect")

    imageOne = cv2.imread(imageOneName, 1)
    imageTwo = cv2.imread(imageTwoName, 1)

    cv2.createTrackbar("Alpha", windowName, 0, 1000, passFunction)

    while True:

        alpha = cv2.getTrackbarPos("Alpha", windowName) / 1000
        beta = 1 - alpha

        output = cv2.addWeighted(imageOne, alpha, imageTwo, beta, 0)

        cv2.imshow(windowName, output)

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
