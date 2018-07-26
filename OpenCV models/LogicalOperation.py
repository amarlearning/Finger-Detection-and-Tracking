import cv2
import matplotlib.pyplot as plt


def main():
    basePath = "../data/"

    imageFileOne = basePath + "4.1.04.tiff"
    imageFileTwo = basePath + "4.1.05.tiff"

    imageOne = cv2.imread(imageFileOne, 1)
    imageTwo = cv2.imread(imageFileTwo, 1)

    imageOneRGB = cv2.cvtColor(imageOne, cv2.COLOR_BGR2RGB)
    imageTwoRGB = cv2.cvtColor(imageTwo, cv2.COLOR_BGR2RGB)

    negativeImage = cv2.bitwise_not(imageOneRGB)
    andImage = cv2.bitwise_and(imageOneRGB, imageTwoRGB)
    orImage = cv2.bitwise_or(imageOneRGB, imageTwoRGB)
    xorImage = cv2.bitwise_xor(imageOneRGB, imageTwoRGB)

    imageNames = [imageOneRGB, imageTwoRGB, negativeImage, andImage, orImage, xorImage]
    imageTitles = ["Image One", "Image Two", "Negative", "AND", "OR", "XOR"]

    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(imageNames[i])
        plt.title(imageTitles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()


if __name__ == "__main__":
    main()
