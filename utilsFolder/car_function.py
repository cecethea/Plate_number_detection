import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
import numpy
import pandas 

path_data = '../data/'
path_source_images = path_data + 'imageAnnoted/images/'

images_dest_folder = 'imageTransform/'
images_dest_folder_2 = 'imageTransform_2/'
image_dest_resized = path_data + images_dest_folder
image_dest_resized = os.listdir(image_dest_resized)
image_dest_resized.sort()
# link images sources
sources_images = os.listdir(path_source_images)
sources_images.sort()
images_test = path_source_images + sources_images[-1]

path_background_image = '../data/imageTransform_2/'
image_cars = os.listdir(path_background_image)
image_cars.sort()
image_test = path_background_image + image_cars[0]

# Read the image
image = cv.imread(image_test)
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# show original image
# Image gray
image_gray = image

laplacian = cv.Laplacian(image, cv.CV_64F)
ret,thresh1 = cv.threshold(image, 127, 255, cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(image,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(image,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(image,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(image,127,255,cv.THRESH_TOZERO_INV)
contours, hierarchy = cv.findContours(thresh4,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)


sobelx = cv.Sobel(image_gray,cv.CV_64F,1,0,ksize=5)
sobely = cv.Sobel(image_gray,cv.CV_64F,0,1,ksize=5)
plt.imshow(thresh4)
plt.show()