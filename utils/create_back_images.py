


def put_images_background(self, source_image, background_image):
    """ This function the background for the images"""
    small_img = source_image
    large_image = cv.imread(background_image)
    scale_percent = 10
    x_offset = int(small_img.shape[1] * scale_percent / 100)
    y_offset = int(small_img.shape[0] * scale_percent / 100)
    large_image[y_offset:y_offset + small_img.shape[0],
    x_offset:x_offset + small_img.shape[1]] = small_img
    return large_image


def create_backround_image(self, image_name):
    """ Create image background"""
    image_gray = cv.imread(image_name)
    image_gray = cv.resize(image_gray, (600, 450), interpolation=cv.INTER_AREA)
    rows, cols = image_gray.shape[:2]
    # cols-1 and rows-1 are the coordinate limits.
    rotation_matrix = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 0, 1)
    image_rotation = cv.warpAffine(image_gray, rotation_matrix, (cols, rows))
    image_name = image_name.split('.')
    image_name = str(image_name[0])
    # Save the rotation images
    try:
        os.mkdir(images_dest_path)
        print("Directory ", images_dest_folder, " Created ")
    except FileExistsError:
        print("Directory ", images_dest_folder, " already exists")

    try:
        cv.imwrite(os.path.join(images_dest_path, image_name + 'BA' + '.jpg'), image_gray)
        print(" File ", image_name, " Created ")
    except FileExistsError:
        print(" File ", image_name, " already exists ")

    plt.imshow(image_rotation)
    plt.show()