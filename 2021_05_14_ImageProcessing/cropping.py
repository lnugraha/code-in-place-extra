import cv2

def main():
    lena = cv2.imread("./images/lena.png")
    height = lena.shape[0]
    width = lena.shape[1]

    # Determine your initial position that you want to crop
    y_init = 125
    x_init = 125

    # Determine the size of the final image that you want to crop
    y_size = 300
    x_size = 300

    # Finalize your modified image
    lena_modified = lena[y_init:y_init+y_size ,x_init:x_init+x_size]

    # Save your image
    cv2.imwrite("./results/lena_cropped.png",lena_modified)

if __name__ == "__main__":
    main()
