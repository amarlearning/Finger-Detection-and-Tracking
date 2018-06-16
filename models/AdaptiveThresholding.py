import cv2
import matplotlib.pyplot as plt


def main():
    const = 2
    block_size = 51
    basePath = "../data/"
    imagePath = basePath + "5.1.12.tiff"

    image = cv2.imread(imagePath, 0)

    mean_thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, const)
    gaussian_thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size,
                                            const)

    images = [image, mean_thresh, gaussian_thresh]
    titles = ["Orignals", "Mean", "Gaussian"]

    for i in range(3):
        plt.subplot(3, 1, i + 1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])

    plt.show()


if __name__ == '__main__':
    main()
