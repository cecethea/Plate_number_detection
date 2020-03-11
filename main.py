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

