import os
import random
import cv2 as cv
import matplotlib.pyplot as plt
from utils_image import GeometricTransformations

# like path --------------------------------------------
path_data = '../data/'
path_source_images = path_data + 'imageAnnoted/images/'
path_background_image = '../data/backImage/back_image.jpg'
images_dest_folder = 'imageTransform/'
images_dest_folder_2 = 'imageTransform_2/'
image_dest_resized = path_data + images_dest_folder
image_dest_resized = os.listdir(image_dest_resized)
image_dest_resized.sort()
# link images sources
sources_images = os.listdir(path_source_images)
sources_images.sort()
images_test = path_source_images + sources_images[0]


# -------------------------------------------------------

# function to transform all images

def resized_all_images():
    change_image = GeometricTransformations()
    change_image.translation
    change_image.rotation
    change_image.perspective_transformation

    for i in range(0, len(sources_images)):
        image_resized = change_image.resized_images(path_source_images + sources_images[i])
        image_resized = change_image.rotation(image_resized)
        sources_images[i] = sources_images[i].split('.')
        sources_images[i] = sources_images[i][0]
        try:
            os.mkdir(path_data + images_dest_folder)
            print("Directory ", images_dest_folder, " Created ")
        except FileExistsError:
            print("Directory ", images_dest_folder, " already exists")

        try:
            cv.imwrite(os.path.join(path_data + images_dest_folder, sources_images[i] + 'RE' + '.jpg'), image_resized)
            print(" File ", sources_images[i], " Created ")
        except FileExistsError:
            print(" File ", sources_images[i], " already exists ")


def create_fond_all_images():
    """ """
    change_image = GeometricTransformations()
    for i in range(0, len(image_dest_resized)):
        image_resized = change_image.put_images_background(path_data + images_dest_folder  + image_dest_resized[i], path_background_image)
        image_dest_resized[i] = image_dest_resized[i].split('.')
        image_dest_resized[i] = image_dest_resized[i][0]
        try:
            os.mkdir(path_data + images_dest_folder_2)
            print("Directory ", images_dest_folder, " Created ")
        except FileExistsError:
            print("Directory ", images_dest_folder, " already exists")

        try:
            cv.imwrite(os.path.join(path_data + images_dest_folder_2, image_dest_resized[i] + '_' + str(i) + '.jpg'), image_resized)
            print(" File ", sources_images[i], " Created ")
        except FileExistsError:
            print(" File ", sources_images[i], " already exists ")

resized_all_images()
#create_fond_all_images()

