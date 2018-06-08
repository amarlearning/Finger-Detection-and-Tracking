import cv2
import time
import numpy as np


def main():

    basePath = "/home/amarpandey/PycharmProjects/OpenCV/data/"

    imageOneName = basePath + "4.1.05.tiff"
    imageTwoName = basePath + "4.1.06.tiff"

    imageOne = cv2.imread(imageOneName, 1)
    imageTwo = cv2.imread(imageTwoName, 1)

    imageOne = cv2.cvtColor(imageOne, cv2.COLOR_BGR2RGB)
    imageTwo = cv2.cvtColor(imageTwo, cv2.COLOR_BGR2RGB)

    for i in np.linspace(0, 1, 100):
        alpha = i
        beta = 1 - alpha
        output = cv2.addWeighted(imageOne, alpha, imageTwo, beta, 0)
        cv2.imshow("Transition", output)
        time.sleep(0.05)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
