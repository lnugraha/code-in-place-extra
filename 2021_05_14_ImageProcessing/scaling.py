"""
May 12, 2021
This program demonstrates how to scale an image (magnifying or shrinking)
"""

import cv2

def main():
    # 1. Load your image then confirm its dimension
    lena   = cv2.imread("./images/lena.png")
    height = lena.shape[0]
    width  = lena.shape[1]
    print(f"The original image has a height of {height} and a width of {width}")

    # 2. Dilate your image
    new_height = 2*height; new_width = 2*width
    lena_dilated = cv2.resize(lena, (new_height, new_width))
    print(f"Image size after dilation has a height of {new_height} and a width of {new_width}")

    # 3. Shrink your image; unlike image dilation, 
    # shrinking image requires a scaling factor that is smaller than 1
    # Unfortunately, cv2.resize function does not support any scaling factor 
    # that is less than 1
    # But never fear, there is one approach to anticipate this issue; 
    # that is using division (// operator)
    """
    Approach (a) using full version
    half_factor = 0.5
    lena_half = cv2.resize(lena, (0, 0), fx=half_factor, fy=half_factor)
    half_height = lena_half.shape[0]
    half_width  = lena_half.shape[1]
    """

    """
    Approach (b) using shortcut
    """
    half_height = height // 2; half_width = width // 2
    lena_half = cv2.resize(lena, (half_height, half_width))
    print(f"Image size after reduction has a height of {half_height} and a width of {half_width}")
    # 4. Check that the dimension is correct then save your image
    cv2.imwrite("./results/lena_doubled.png", lena_dilated)        
    cv2.imwrite("./results/lena_shrunk.png", lena_half)

if __name__ == "__main__":
    main()
