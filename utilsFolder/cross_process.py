# import the necessary packages
import numpy as np
import cv2 as cv 
import os
import matplotlib.pyplot as plt

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

class CropPreprocessor:
    def __init__(self, width = 100, height = 150, horiz=True, inter=cv.INTER_AREA):
        # store the target image width, height, whether or not
        # horizontal flips should be included, along with the
        # interpolation method used when resizing
        self.width = width
        self.height = height
        self.horiz = horiz
        self.inter = inter
    def preprocess(self, image):
        # initialize the list of crops crops = []
        # grab the width and height of the image then use these
        # dimensions to define the corners of the image based 
        (h, w) = image.shape[:2]
        coords = [
        [0, 0, self.width, self.height],
        [w - self.width, 0, w, self.height],
        [w - self.width, h - self.height, w, h], [0, h - self.height, self.width, h]]
        # compute the center crop of the image as well
        dW = int(0.5 * (w - self.width))
        dH = int(0.5 * (h - self.height)) 
        coords.append([dW, dH, w - dW, h - dH])
        # loop over the coordinates, extract each of the crops, # and resize each of them to a fixed size
        for (startX, startY, endX, endY) in coords:
            crops = []
            crop = image[startY:endY, startX:endX]
            crop = cv.resize(crop, (self.width, self.height),interpolation=self.inter) 
            crops.append(crop)
            
            # check to see if the horizontal flips should be taken
            if self.horiz:
                # compute the horizontal mirror flips for each crop 
                mirrors = [cv.flip(c, 1) for c in crops] 
                crops.extend(mirrors)
                # return the set of crops
        return np.array(crops)

image_array = CropPreprocessor()
image = cv.imread(image_test)
func = image_array.preprocess(image)
plt.imshow(func[1:2])
plt.show
print(func)
