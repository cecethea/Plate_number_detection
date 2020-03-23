import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

path_background_image = '../data/imageTransform_2/'
image_cars = os.listdir(path_background_image)
image_cars.sort()
image_test = path_background_image + image_cars[1]


# Read the image
image = cv.imread(image_test)
# show original image

# Image gray
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#plt.imshow(image_gray)
#plt.show()

# Bylateral image
image_gray = cv.bilateralFilter(image_gray, 11, 17, 17)
#plt.imshow(image_by)
#plt.show()

# image edge
edge = cv.Canny(image_gray, 170, 200)
#plt.imshow(edge)
#plt.show()

# find contour
cnts, new = cv.findContours(edge.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# draw contour
image_1 = image.copy()
cv.drawContours(image_1, cnts, -1, (0, 255, 0), 3)
#plt.imshow(image_1)
#plt.show()
# sorted area
#cnts = sorted(cnts, key= cv.contourArea, reverse= True)[:220]
NumberPlateCnt = None
image_2 = image.copy()
cv.drawContours(image_2, cnts, -1, (0, 255, 0), 3)
#plt.imshow(image_2)
#plt.show()

# lops
count = 0
idx = 7
for c in cnts:
    print(c)
    peri = cv.arcLength(c, True)
    approx = cv.approxPolyDP(c, 0.2 * peri, True)
    if len(approx) == 4 :
        NumberPlateCnt = approx
        x, y, w, h = cv.boundingRect(c)
        new_image = image[y:y + h, x:x + w]
        cv.imwrite('Image' + str(idx) + '.png', new_image)
        idx += 1
        break

image_3 = image.copy()
cv.drawContours(image_3, NumberPlateCnt, -1, (0, 255, 0), 3)
plt.imshow(image_3)
plt.show()



