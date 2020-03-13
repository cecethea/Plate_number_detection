

def resized_images(self, images_name):
    """ This function resized the images """
    img = cv.imread(images_name, cv.IMREAD_UNCHANGED)
    scale_percent = random.choice([20, 10, 35, 9, 17])
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    image_resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
    try:
        os.mkdir(images_dest_path_1)
        print("Directory ", images_dest_folder_1, " Created ")
    except FileExistsError:
        print("Directory ", images_dest_folder_1, " already exists")

    try:
        cv.imwrite(os.path.join(images_dest_path_1, images_name), image_resized)
        print(" File ", images_name, " Created ")
    except FileExistsError:
        print(" File ", images_name, " already exists ")
    return image_resized