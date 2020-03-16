import os
import random
import cv2 as cv
import matplotlib.pyplot as plt
from utilsFolder import transform_images
# like data --------------------------------------------
data_path = '../data/'
images_path_source = data_path + 'imageAnnoted/images/'
backg_image = '../data/backImage/back_image.jpg'
images_name = os.listdir(images_path_source)
images_name.sort()
images_name = images_path_source + images_name[0]
# -------------------------------------------------------
image_parametere = transform_images()

def resized_images(images_name):
    """ This function resized the images """
    img = cv.imread(images_name, cv.IMREAD_UNCHANGED)
    scale_percent = random.choice([20, 10, 35, 9, 17])
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    image_resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
    # save images resized in the folders
    return image_resized


def put_images_background(source_image, background_image):
    """ This function the background for the images"""
    small_img = cv.imread(source_image)
    large_image = cv.imread(background_image)
    rows, cols, ch = small_img.shape
    print(small_img.shape)
    rows = rows * 2
    cols = cols * 2
    large_image = cv.resize(large_image, (cols, rows), interpolation=cv.INTER_AREA)
    scale_percent = 50
    x_offset = int(small_img.shape[1] * scale_percent / 100)
    y_offset = int(small_img.shape[0] * scale_percent / 100)
    large_image[y_offset:y_offset + small_img.shape[0],
    x_offset:x_offset + small_img.shape[1]] = small_img
    return large_image


image_re = resized_images(images_name)
cv.imwrite('image_test.jpg', image_re)
image_sou = '../data/backImage/image_test.jpg'
image_large = put_images_background(image_sou, backg_image)
cv.imwrite('large_image.jpg', image_large)
plt.imshow(image_large)
plt.show()
