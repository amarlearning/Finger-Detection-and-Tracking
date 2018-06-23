import cv2


def main():
    image = cv2.imread("../data/4.2.07.tiff", 1)
    cv2.imshow("Orignal Image", image)

    output = cv2.Canny(image, 100, 151, apertureSize=3, L2gradient=True)
    cv2.imshow("Edge Detected Image", output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
