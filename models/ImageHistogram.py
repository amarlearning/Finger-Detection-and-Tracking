import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("../data/4.1.03.tiff", 0)

plt.subplot(2, 1, 1)
plt.imshow(image, cmap="gray")
plt.title("Orignal Image")

plt.subplot(2, 1, 2)
plt.hist(image.ravel(), 256, [0, 255])
plt.xlim([0, 255])
plt.title("Image Histogram")

plt.show()