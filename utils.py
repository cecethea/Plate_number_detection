import os
import numpy as np
import pandas as pd
import cv2 as cv
import matplotlib.pyplot as plt

# declare of variable global
folder_dataset = './data/'
images_source_path = folder_dataset + 'imageAnnoted/'
images_name_source = os.listdir(images_source_path)
images_name_source.sort()

# images destination variable
images_dest_folder = 'imagesTransform'
images_dest_path = folder_dataset + images_dest_folder + '/'

# select a test image
image_test = images_name_source[0]


class GeometricTransformations:
    """ Geometric Transformations of images """

    # def __init__(self, images_name=None):
    #     """ initialize data"""
    #     self.images = images_name

    @classmethod
    def translation(self, image_name):
        """ Images translation function """
        image_gray = cv.imread(images_source_path + image_name, 0)
        rows, cols = image_gray.shape[:2]
        M = np.float32([[1, 0, 100], [0, 1, 50]])
        dst = cv.warpAffine(image_gray, M, (cols, rows))
        plt.imshow(dst)
        plt.show()

    @classmethod
    def rotation(self, image_name):
        """ Images rotation function """
        image_gray = cv.imread(images_source_path + image_name, 0)
        rows, cols = image_gray.shape[:2]
        # cols-1 and rows-1 are the coordinate limits.
        rotation_matrix = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 10, 1)
        image_rotation = cv.warpAffine(image_gray, rotation_matrix, (cols, rows))

        # Save the rotation images
        try:
            os.mkdir(images_dest_path)
            print("Directory ", images_dest_folder, " Created ")
        except FileExistsError:
            print("Directory ", images_dest_folder, " already exists")

        try:
            cv.imwrite(os.path.join(images_dest_path, image_name), rotation_matrix)
            print(" File ", image_name, " Created ")
        except FileExistsError:
            print(" File ", image_name, " already exists ")

        plt.imshow(image_rotation)
        plt.show()

    def perspective_transformation(self, image_name):
        """ Perspective transformation  """
        image_gray = cv.imread(images_source_path + image_name, 0)
        rows, cols = image_gray.shape
        pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
        pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
        matrix_perspective = cv.getPerspectiveTransform(pts1, pts2)
        image_perspective = cv.warpPerspective(image_gray, matrix_perspective, (300, 300))
        # input image
        plt.subplot(121), plt.imshow(image_gray), plt.title('Input')
        # Output image
        plt.subplot(122), plt.imshow(image_perspective), plt.title('Output')
        # Show function
        plt.show()


if __name__ == "__main__":
    change_images = GeometricTransformations()
    change_images.translation(image_test)
    change_images.rotation(image_test)
    change_images.perspective_transformation(image_test)
