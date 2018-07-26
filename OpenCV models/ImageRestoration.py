import cv2


def main():
    image = cv2.imread("../data/Damaged Image.tiff", 1)
    mask_image = cv2.imread("../data/Mask.tiff", 0)

    telea_image = cv2.inpaint(image, mask_image, 5, cv2.INPAINT_TELEA)
    ns_image = cv2.inpaint(image, mask_image, 5, cv2.INPAINT_NS)

    cv2.imshow("Orignal Image", image)
    cv2.imshow("Mask Image", mask_image)

    cv2.imshow("TELEA Restored Image", telea_image)
    cv2.imshow("NS Restored Image", ns_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
