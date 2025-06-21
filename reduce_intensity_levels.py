import cv2
import numpy as np

def reduce_intensity_levels(image_path, levels):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: Could not read image.")
        return

    if levels < 2 or levels > 256 or (levels & (levels - 1)) != 0:
        raise ValueError("Levels must be a power of 2 and <= 256 (e.g., 2, 4, 8, ..., 256)")

    factor = 256 // levels
    reduced_image = (image // factor) * factor
    reduced_image = reduced_image.astype(np.uint8)

    output_path = f"reduced_levels_{levels}.jpg"
    cv2.imwrite(output_path, reduced_image)
    print(f"Saved reduced image to: {output_path}")

    cv2.imshow(f"Reduced to {levels} levels", reduced_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = input("Enter the path to the input image: ")

    while True:
        try:
            levels = int(input("Enter the desired number of intensity levels (power of 2, up to 256): "))
            if levels < 2 or levels > 256 or (levels & (levels - 1)) != 0:
                print("Invalid input. Levels must be a power of 2 and <= 256.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    reduce_intensity_levels(image_path, levels)
