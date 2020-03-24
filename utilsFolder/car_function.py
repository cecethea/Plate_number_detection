import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

path_background_image = '../data/imageTransform_2/'
image_cars = os.listdir(path_background_image)
image_cars.sort()
image_test = path_background_image + image_cars[5]


# Read the image
image = cv.imread(image_test)
# show original image

# Image gray
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
thresh, image_binarized = cv.threshold(image_gray, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
edge = cv.Canny(image_binarized, 100, 200)
image_blue = cv.blur(edge, (5, 5))
contours, hierarchy = cv.findContours(image_blue, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(image_blue, contours, -1, (0, 255, 0), 3)
plt.imshow(edge)
plt.show()




