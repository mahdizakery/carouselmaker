# Automatic Photo Slicer and Framer for Social Media Carousel View

This Python script uses OpenCV to slice an input image into two equal halves on the x-axis, create a white background photo with the same width and height as one of the sliced images, and paste the original photo inside that background with resizing. It can process multiple images at once in a specified directory and store the output images in separate folders with the names of the original images.

# Prerequisites

- Python 3
- OpenCV
- Numpy

# Usage

Run the script with the following command:

<code> python script.py [path] </code>

- [path] (optional): Path to the directory containing the input images. If not specified, the script will use the directory of the script.
  The script will process all image files in the specified directory and save the output images in subdirectories with the names of the original images.

Note: The script will only process image files with extensions .jpg, .jpeg, .png, .bmp.

# Output

The script will output three images for each input image:

- left.jpg: The left half of the original image.
- right.jpg: The right half of the original image.
- framed.jpg: The original image resized to 49% of its original size and centered on a white background with the same width and height as one of the sliced images.
  Each set of three images will be saved in a subdirectory with the same name as the original image in the output_images directory.
