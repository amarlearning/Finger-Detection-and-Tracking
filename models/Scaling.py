import cv2


def main():
    imageOne = cv2.imread("../data/4.1.04.tiff", 1)

    areaInter = cv2.resize(imageOne, None, fx=3, fy=3, interpolation=cv2.INTER_AREA)
    cubicInter = cv2.resize(imageOne, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    linearInter = cv2.resize(imageOne, None, fx=3, fy=3, interpolation=cv2.INTER_LINEAR)
    nearestInter = cv2.resize(imageOne, None, fx=3, fy=3, interpolation=cv2.INTER_NEAREST)
    lancz0s4Inter = cv2.resize(imageOne, None, fx=3, fy=3, interpolation=cv2.INTER_LANCZOS4)

    cv2.imshow("Area Interpolation Image", areaInter)
    cv2.imshow("Cubic Interpolation Image", cubicInter)
    cv2.imshow("Linear Interpolation Image", linearInter)
    cv2.imshow("Nearest Interpolation Image", nearestInter)
    cv2.imshow("LANCZ0S4 Interpolation Image", lancz0s4Inter)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
