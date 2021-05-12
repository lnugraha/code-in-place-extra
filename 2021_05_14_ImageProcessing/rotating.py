"""
May 12, 2021
This program demonstrates image rotation methods
"""

import cv2
import math

def main():
    # 1. Load your original image
    lena = cv2.imread("./images/lena.png")

    # 2. Image rotation here; assume rotate by 90 deg or 180 deg or 270 deg
    # Only select those 3 angles to avoid unnecessary image interpolation
    

    # 3. Save your modified image
    cv2.imwrite("./results/lena_rotated.png", lena_modified)

if __name__ == "__main__":
    main()
