"""
May 12, 2021
Add border surrounding an image
The border color can also be changed with the provided color
"""

import cv2
import numpy as np

def main():
    # 1. Load your image
    original_img = cv2.imread("./images/simba-sq.jpg")
    height = original_img.shape[0]
    width = original_img.shape[1]
    print("Height: {}, width: {}".format(height, width))
    
    # 2. Add border surrounding the image
    # Say border thickness is 30 pixels
    # Begin by creating a new canvas
    border = 30
    new_height = height + 2*border
    new_width  = width + 2*border
    new_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)


    # 3. Save the image

if __name__ == "__main__":
    main()
