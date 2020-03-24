import os

path_data = '../data/'
path_source_images = path_data + 'imageAnnoted/text/'
# link images sources
sources_images = os.listdir(path_source_images)
sources_images.sort()
folder_image_rename = path_data + 'textRename/'

for i in range(0, len(sources_images)):
    old_file = os.path.join(path_source_images, sources_images[i])
    new_file = os.path.join(folder_image_rename, '{0:04}'.format(i) + '.txt')
    os.rename(old_file, new_file)
