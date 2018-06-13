import cv2


def main():

    basePath = "../data/"
    imageOneFile = basePath + "4.1.04.tiff"

    imageOne = cv2.imread(imageOneFile, 1)

    output = cv2.resize(imageOne, )

    cv2.imshow("Resized Image", imageOne)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()