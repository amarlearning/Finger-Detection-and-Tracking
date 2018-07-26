import cv2


def passFunction(x):
    pass


def main():
    windowName = "Transition Effect"

    cv2.namedWindow("Transition Effect")

    imageOne = cv2.imread("../data/lena_color_512.tif", 1)
    imageTwo = cv2.imread("../data/mandril_color.tif", 1)

    cv2.createTrackbar("Alpha", windowName, 0, 1000, passFunction)

    while True:

        alpha = cv2.getTrackbarPos("Alpha", windowName) / 1000
        beta = 1 - alpha

        output = cv2.addWeighted(imageOne, alpha, imageTwo, beta, 0)

        cv2.imshow(windowName, output)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
