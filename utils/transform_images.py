import os
import numpy as np
import cv2 as cv


class GeometricTransformations:
    """ Geometric Transformations of images """

    @classmethod
    def translation(self, image_name):
        """ Images Translation function """
        image_gray = cv.imread(image_name)
        rows, cols = image_gray.shape[:2]
        matrix_translation = np.float32([[1, 0, 100], [0, 1, 50]])
        image_translation = cv.warpAffine(image_gray, matrix_translation, (cols, rows))
        image_translation = cv.blur(image_translation, (5, 5))
        return image_translation

    @classmethod
    def rotation(self, image_name):
        """ Images Rotation function """
        image_gray = cv.imread(image_name)
        rows, cols = image_gray.shape[:2]
        # cols-1 and rows-1 are the coordinate limits.
        rotation_matrix = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 10, 1)
        image_rotation = cv.warpAffine(image_gray, rotation_matrix, (cols, rows))
        return image_rotation

    @classmethod
    def perspective_transformation(self, image_name):
        """ Images Perspective transformation  """
        image_gray = cv.imread(image_name)
        rows, cols, ch = image_gray.shape
        pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
        pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
        matrix_perspective = cv.getPerspectiveTransform(pts1, pts2)
        image_perspective = cv.warpPerspective(image_gray, matrix_perspective, (cols, rows))
        return image_perspective

    def media_bleu_images(self, image_name):
        """ Images Bleu transformation """
        image_gray = cv.imread(image_name)
        rows, cols, ch = image_gray.shape
        image_bleu = cv.blur(image_gray, (5, 5))
        image_bleu = cv.flip(image_bleu, -1)
        return image_bleu


if __name__ == "__main__":
    change_images = GeometricTransformations()
