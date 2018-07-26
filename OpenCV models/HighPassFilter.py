import cv2


def main():
    image = cv2.imread("../data/5.1.11.tiff", 0)
    cv2.imshow("Orignal Image", image)

    # Laplacian High Pass Filter
    lap_filter = cv2.Laplacian(image, ddepth=-1, ksize=7, scale=1, borderType=cv2.BORDER_DEFAULT)
    cv2.imshow("Laplacian Filter", lap_filter)

    # Sobel High Pass Filter
    sobelx_filter = cv2.Sobel(image, ddepth=-1, dx=2, dy=0, ksize=7, scale=1, borderType=cv2.BORDER_DEFAULT)
    cv2.imshow("Sobel X Filter", sobelx_filter)

    sobely_filter = cv2.Sobel(image, ddepth=-1, dx=0, dy=2, ksize=7, scale=1, borderType=cv2.BORDER_DEFAULT)
    cv2.imshow("Sobel Y Filter", sobely_filter)

    sobel_filter = sobelx_filter + sobely_filter
    cv2.imshow("Sobel Filter", sobel_filter)

    # Scharr High Pass Filter Implementation
    scharrx_filter = cv2.Scharr(image, ddepth=-1, dx=1, dy=0, scale=1, borderType=cv2.BORDER_DEFAULT)
    cv2.imshow("Scharr X Filter", scharrx_filter)

    scharry_filter = cv2.Scharr(image, ddepth=-1, dx=0, dy=1, scale=1, borderType=cv2.BORDER_DEFAULT)
    cv2.imshow("Scharr Y Filter", scharry_filter)

    scharr_filter = scharrx_filter + scharry_filter
    cv2.imshow("Scharr Filter", scharr_filter)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
