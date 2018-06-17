import random

import cv2
import matplotlib.pyplot as plt


def main():
    probability = 0.05  # only 5% of the total image will have noise
    imagepath = "../data/4.1.08.tiff"
    imagebgr = cv2.imread(imagepath, 1)
    imagergb = cv2.cvtColor(imagebgr, cv2.COLOR_BGR2RGB)

    rows, columns, channels = imagergb.shape

    for i in range(rows):
        for j in range(columns):
            rand = random.random()
            if rand < (probability / 2):
                # pepper noise
                imagergb[i][j] = [0, 0, 0]
            elif rand < probability:
                # salt noise
                imagergb[i][j] = [255, 255, 255]
            else:
                pass

    plt.imshow(imagergb)
    plt.title("Salt and Pepper Noise Image")
    plt.show()


if __name__ == '__main__':
    main()
