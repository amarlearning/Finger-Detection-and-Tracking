import cv2
import numpy as  np


def main():
    image = cv2.imread("../data/detect_blob.png", 1)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    binay_thresh = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

    _, contours, _ = cv2.findContours(binay_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    new_image = np.zeros((image.shape[0], image.shape[1], 3), np.uint8)

    for cnt in contours:
        cv2.drawContours(new_image, [cnt], -1, (255, 0, 255), -1)

        # get contour area using 'contourArea' method
        area_cnt = cv2.contourArea(cnt)

        # get the perimeter of any contour using 'arcLength'
        perimeter_cnt = cv2.arcLength(cnt, True)

        # get centroid oy contour using moments
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])

        cv2.circle(new_image, (cx, cy), 3, (0, 255, 0), -1)

        print("Area : {}, Perimeter : {}".format(area_cnt, perimeter_cnt))

    cv2.imshow("Contoured Image", new_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
