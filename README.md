# EC7212-Take-Home-Assignment-1

This repository contains four separate Python scripts for common image processing tasks using OpenCV and NumPy. Each script interactively asks for the input image path and parameters (if any), processes the image, saves the output images, and displays them.

---

## Table of Contents

- [Requirements](#requirements)  
- [Installation](#installation)  
- [Scripts Overview](#scripts-overview)  
- [How to Run](#how-to-run)  
- [Notes](#notes)  
- [Author](#author)  

---

## Requirements

- Python 3.6 or later  
- OpenCV (`opencv-python`)  
- NumPy

---

## Installation

1. **Install Python**  
   Download and install Python from [python.org](https://www.python.org/downloads/) if not already installed.

2. **Install dependencies**  
   Run the following command in your terminal or command prompt:

   ```bash
   pip install opencv-python numpy

##Scripts Overview

1. **reduce_intensity_levels.py**
Reduces the number of grayscale intensity levels in an image to a specified power-of-two number (e.g., 2, 4, 8, 16, ...).

2. **apply_spatial_averaging.py**
Applies spatial averaging (mean filtering) on a grayscale image using neighborhoods of sizes 3x3, 10x10, and 20x20.

3. **rotate_image.py**
Rotates the input image by 45 degrees and 90 degrees, saving and displaying both results.

4. **block_average.py**
Performs block averaging with non-overlapping blocks of sizes 3x3, 5x5, and 7x7, replacing each block's pixels with their average color.

##How to Run

Open your terminal or command prompt.

Change directory to where the scripts and images are located:

  bash
  ` ``` cd path/to/your/folder `

Run the desired script by typing:

  bash
  ` ```python script_name.py`
  
When prompted, enter the path to your input image (relative or absolute path).

For the intensity reduction script, also enter the number of intensity levels (power of 2, max 256).

Output images will be saved in the same folder with descriptive filenames.

Processed images will display in windows — press any key to close.

##Notes

Supported image formats depend on OpenCV (commonly JPG, PNG, BMP, etc.).

Intensity levels for reduce_intensity_levels.py must be a power of 2 and ≤ 256.

Blocks smaller than the specified size at image edges are ignored in block_average.py.

Windows displaying images require keyboard input to close.

##Author

Kavinda Sandamal
Date: 2025-06-21


