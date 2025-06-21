import cv2
import numpy as np

def block_average(image_path, block_sizes=[3, 5, 7]):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found.")
        return

    h, w = image.shape[:2]

    for block_size in block_sizes:
        result = np.copy(image)
        for y in range(0, h, block_size):
            for x in range(0, w, block_size):
                block = image[y:y+block_size, x:x+block_size]
                if block.shape[0] != block_size or block.shape[1] != block_size:
                    continue
                avg_color = block.mean(axis=(0, 1)).astype(np.uint8)
                result[y:y+block_size, x:x+block_size] = avg_color

        output_name = f"block_avg_{block_size}x{block_size}.jpg"
        cv2.imwrite(output_name, result)
        print(f"Saved: {output_name}")
        cv2.imshow(f"{block_size}x{block_size} Block Averaging", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = input("Enter the path to the input image: ")
    block_average(image_path)
