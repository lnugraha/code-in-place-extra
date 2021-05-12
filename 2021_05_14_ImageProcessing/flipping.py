"""
May 12, 2021
This program demonstrates image rotation methods
"""

import cv2
import math

def main():
    # 1. Load your original image
    lena = cv2.imread("./images/lena.png")

    # 2. Image flip here
    # Three possible image flip positions
    # 0: vertical flip
    # 1: horizontal flip
    # -1: both vertical and horizontal flip
    flip_code = 1 # mirroring
    lena_modified = cv2.flip(lena, flip_code)

    # 3. Save your modified image
    cv2.imwrite("./results/lena_mirrored.png", lena_modified)

if __name__ == "__main__":
    main()
