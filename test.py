from seam_carving import SeamCarver

import os



def image_resize_without_mask(filename_input, filename_output):
    print("start conversion...")
    obj = SeamCarver(filename_input)
    obj.save_result(filename_output)
    print("finish conversion")

if __name__ == '__main__':
    """
    Put image in in/images folder and protect or object mask in in/masks folder
    Ouput image will be saved to out/images folder with filename_output
    """

    folder_in = 'in'
    folder_out = 'out'

    filename_input = 'image.png'
    filename_output = 'image_result.png'
    filename_mask = 'mask.jpg'

    input_image = os.path.join(folder_in, "images", filename_input)
    output_image = os.path.join(folder_out, "images", filename_output)


    image_resize_without_mask(input_image, output_image)







