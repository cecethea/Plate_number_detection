import os
import numpy as np
import pandas as pd
import cv2 as cv
import matplotlib.pyplot as plt

# import the files path 
files_path = './data/imageAnnoted/'
images_path = os.listdir(files_path)
images_path.sort()
image_1 = images_path[0]
image_1 = cv.imread(files_path + image_1)
image_gray = cv.cvtColor(image_1, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(image_gray, 127, 255, 0)
# calculate the contours from binary image
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
with_contours = cv.drawContours(image_1, contours, -1, (0, 255, 0), 3)
plt.imshow(with_contours)
plt.show()
