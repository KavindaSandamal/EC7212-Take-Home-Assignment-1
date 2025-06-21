import cv2
import numpy as np

def apply_spatial_averaging(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: Could not load image.")
        return

    for size in [3, 10, 20]:
        kernel = np.ones((size, size), np.float32) / (size * size)
        averaged = cv2.filter2D(image, -1, kernel)
        filename = f"averaged_{size}x{size}.jpg"
        cv2.imwrite(filename, averaged)
        print(f"Saved: {filename}")
        cv2.imshow(f"{size}x{size} Averaging", averaged)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = input("Enter the path to the input image: ")
    apply_spatial_averaging(image_path)
