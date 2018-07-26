import cv2
import matplotlib.pyplot as plt


def main():
    threshold = 0
    max_value = 255

    image = cv2.imread("../data/7.1.08.tiff", 0)

    # when applying OTSU threshold, set threshold to 0.

    _, output1 = cv2.threshold(image, threshold, max_value, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    _, output2 = cv2.threshold(image, threshold, max_value, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    _, output3 = cv2.threshold(image, threshold, max_value, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
    _, output4 = cv2.threshold(image, threshold, max_value, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)
    _, output5 = cv2.threshold(image, threshold, max_value, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)

    images = [image, output1, output2, output3, output4, output5]
    titles = ["Orignals", "Binary", "Binary Inverse", "TOZERO", "TOZERO INV", "TRUNC"]

    for i in range(6):
        plt.subplot(3, 2, i + 1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])

    plt.show()


if __name__ == '__main__':
    main()
