import cv2
import matplotlib.pyplot as plt


def main():
    basePath = "../data/"
    imagePath = basePath + "house.tiff"

    image = cv2.imread(imagePath, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    _, output1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    _, output2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    _, output3 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
    _, output4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
    _, output5 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)

    images = [image, output1, output2, output3, output4, output5]
    titles = ["Orignals", "Binary", "Binary Inverse", "TOZERO", "TOZERO INV", "TRUNC"]

    for i in range(6):
        plt.subplot(3, 2, i + 1)
        plt.imshow(images[i])
        plt.title(titles[i])

    plt.show()


if __name__ == '__main__':
    main()
