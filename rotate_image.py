import cv2

def rotate_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found.")
        return

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    matrix_45 = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated_45 = cv2.warpAffine(image, matrix_45, (w, h))

    matrix_90 = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated_90 = cv2.warpAffine(image, matrix_90, (w, h))

    cv2.imwrite("rotated_45.jpg", rotated_45)
    cv2.imwrite("rotated_90.jpg", rotated_90)
    print("Saved: rotated_45.jpg and rotated_90.jpg")

    cv2.imshow("Rotated 45 Degrees", rotated_45)
    cv2.imshow("Rotated 90 Degrees", rotated_90)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = input("Enter the path to the input image: ")
    rotate_image(image_path)
