import numpy as np
import cv2 as cv
import random


class GeometricTransformations:
    """ Geometric Transformations of images """

    @classmethod
    def resized_images(self, images_name):
        """ This function resized the images """
        img = cv.imread(images_name, cv.IMREAD_UNCHANGED)
        scale_percent = random.choice([20, 10, 35, 9, 17])
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        image_resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
        return image_resized

    @classmethod
    def translation(self, image_name):
        """ Images Translation function """
        image_gray = image_name
        rows, cols = image_gray.shape[:2]
        matrix_translation = np.float32([[1, 0, 100], [0, 1, 50]])
        image_translation = cv.warpAffine(image_gray, matrix_translation, (cols * 2, rows * 2))
        image_translation = cv.blur(image_translation, (5, 5))
        return image_translation

    @classmethod
    def rotation(self, image_name):
        """ Images Rotation function """
        image_gray = image_name
        rows, cols = image_gray.shape[:2]
        # cols-1 and rows-1 are the coordinate limits.
        rotation_matrix = cv.getRotationMatrix2D((rows/2.0, cols/2.0), 10, 1)
        image_rotation = cv.warpAffine(image_gray, rotation_matrix, (cols * 2, rows * 3))
        return image_rotation

    @classmethod
    def perspective_transformation(self, image_name):
        """ Images Perspective transformation  """
        image_gray = image_name
        rows, cols, ch = image_gray.shape
        pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
        pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
        matrix_perspective = cv.getPerspectiveTransform(pts1, pts2)
        image_perspective = cv.warpPerspective(image_gray, matrix_perspective, (cols * 2, rows * 2))
        return image_perspective

    @classmethod
    def media_bleu_images(self, image_name):
        """ Images Bleu transformation """
        image_gray = cv.imread(image_name)
        rows, cols = image_gray.shape
        image_bleu = cv.blur(image_gray, (5, 5))
        image_bleu = cv.flip(image_bleu, -1)
        return image_bleu

    @classmethod
    def put_images_background(self, source_image, background_image):
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


if __name__ == "__main__":
    change_images = GeometricTransformations()
