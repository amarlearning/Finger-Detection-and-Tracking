import cv2


image = cv2.imread("../data/4.2.03.tiff", 1)

low_image = cv2.pyrDown(image)

cv2.imshow("Orignal Image", image)
cv2.imshow("Pyramid Image", low_image)