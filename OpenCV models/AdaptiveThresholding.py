import cv2
import matplotlib.pyplot as plt


def main():
    const = 2
    block_size = 51
    imagePath = "../data/sudoku.png"

    image = cv2.imread(imagePath, 0)

    cv2.imshow("Orignal Image", image)

    mean_thresh = \
        cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, const)
    gaussian_thresh = \
        cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, const)

    images = [image, mean_thresh, gaussian_thresh]
    titles = ["Orignals", "Mean", "Gaussian"]

    cv2.imshow("Mean Image", mean_thresh)
    cv2.imshow("Gaussian Image", gaussian_thresh)

    for i in range(3):
        plt.subplot(3, 1, i + 1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])

    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
