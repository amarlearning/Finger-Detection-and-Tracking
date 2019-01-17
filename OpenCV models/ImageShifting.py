import cv2
import matplotlib.pyplot as plt
import numpy as np


def main():
    imagePath = "../data/4.1.04.tiff"
    shifting = np.float32([[1, 0, 50], [0, 1, 50]])

    image = cv2.imread(imagePath, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    rows, columns, _ = image.shape

    shiftedImage = cv2.warpAffine(image, shifting, (rows, columns))

    plt.imshow(shiftedImage)
    plt.title("Shifted Image")
    plt.show()


if __name__ == '__main__':
    main()
