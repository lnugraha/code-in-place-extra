import cv2

def main():
    original = cv2.imread("./images/mt-rainier.jpg")
    reverse = cv2.flip(original, 0)

    reflectionCombined = cv2.vconcat([original, reverse])
    cv2.imwrite("reflection_rainier.png", reflectionCombined)

if __name__ == "__main__":
    main()
