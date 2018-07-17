import cv2


def main():
    frame = cv2.imread("../data/players.jpg", 0)
    template = cv2.imread("../data/template.jpg", 0)

    result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)

    min_value, max_value, min_loc, max_loc = cv2.minMaxLoc(result)

    cv2.circle(result, max_loc, 20, 255, 1)

    cv2.imshow("Frame Image", frame)
    cv2.imshow("Result Image", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
