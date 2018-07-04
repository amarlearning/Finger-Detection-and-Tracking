import cv2
import matplotlib.pyplot as plt


def main():
    imageOne = cv2.imread("../data/house.tiff", 1)
    imageOne = cv2.cvtColor(imageOne, cv2.COLOR_BGR2RGB)

    red, green, blue = cv2.split(imageOne)

    images = [cv2.merge((red, green, blue)), red, green, blue]
    titles = ["Default RGB Image", "Only Red", "Only Blue", "Only Green"]
    cmaps = ["gray", "Reds", "Greens", "Blues"]

    for i in range(4):
        plt.subplot(2, 2, i + 1)

        plt.imshow(images[i], cmap=cmaps[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()


if __name__ == "__main__":
    main()
