import cv2
import matplotlib.pyplot as plt


def main():
    image = cv2.imread("../data/4.1.03.tiff", 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    red, green, blue = cv2.split(image_rgb)

    eq_red_image = cv2.equalizeHist(red)
    eq_green_image = cv2.equalizeHist(green)
    eq_blue_image = cv2.equalizeHist(blue)

    red_hist = cv2.calcHist([red], [0], None, [256], [0, 255])
    green_hist = cv2.calcHist([green], [0], None, [256], [0, 255])
    blue_hist = cv2.calcHist([blue], [0], None, [256], [0, 255])

    eq_red_hist = cv2.calcHist([eq_red_image], [0], None, [256], [0, 255])
    eq_green_hist = cv2.calcHist([eq_green_image], [0], None, [256], [0, 255])
    eq_blue_hist = cv2.calcHist([eq_blue_image], [0], None, [256], [0, 255])

    channels_images = [red_hist, green_hist, blue_hist]
    equalized_images = [eq_red_hist, eq_green_hist, eq_blue_hist]

    # Channels Histogram
    for i in range(3):
        plt.subplot(4, 1, i + 1)
        plt.plot(channels_images[i], color='g')
        plt.xlim([0, 255])

    plt.show()

    # Channels Equalized Histogram
    for i in range(3):
        plt.subplot(3, 1, i + 1)
        plt.plot(equalized_images[i], color='b')
        plt.xlim([0, 255])

    plt.show()


if __name__ == '__main__':
    main()
