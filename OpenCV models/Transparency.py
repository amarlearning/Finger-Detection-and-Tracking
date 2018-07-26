import cv2


def main():
    image = cv2.imread("../data/house.tiff", 1)

    # Instead of split sue this way, more fast
    blue = image[:, :, 0]
    green = image[:, :, 1]
    red = image[:, :, 2]

    # combine each color spacing with alpha channel
    rgba = cv2.merge((blue, green, red, red))

    # cv2 gui does not support alpha value, so use default OS viewer
    # use png format, because jpeg does not support alpha channel
    print(cv2.imwrite("../data/rgba_red.png", rgba))


if __name__ == '__main__':
    main()
