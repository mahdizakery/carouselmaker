import os
import cv2 as cv
import numpy as np

# Set the output directory
output_dir = 'output_images'

# Find all image files in the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
img_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
img_filenames = [filename for filename in os.listdir(script_dir)
                 if os.path.splitext(filename)[1].lower() in img_extensions]

# Process each image file
for img_filename in img_filenames:
    # Load the image
    img_path = os.path.join(script_dir, img_filename)
    img = cv.imread(img_path)

    # Split the image in half
    height, width, color = img.shape
    frameWidth = np.ceil(width / 2).astype(int)
    left_part = img[:, :frameWidth]
    right_part = img[:, frameWidth:]

    # Create a white background image
    framed = np.zeros((height, frameWidth, 3), np.uint8)
    framed[:, :] = (255, 255, 255)

    # Resize the original image and center it in the framed image
    scale = 49
    w = int(img.shape[1] * scale / 100)
    h = int(img.shape[0] * scale / 100)
    dim = (w, h)
    resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
    h_resized, w_resized, _ = resized.shape

    x_center = int(framed.shape[1] / 2 - w_resized / 2)
    y_center = int(framed.shape[0] / 2 - h_resized / 2)
    framed[y_center:y_center + h_resized, x_center:x_center + w_resized] = resized

    # Create a directory for the output images
    output_subdir = os.path.join(output_dir, os.path.splitext(img_filename)[0])
    os.makedirs(output_subdir, exist_ok=True)

    # Save the left, right, and framed images to the output directory
    left_output_path = os.path.join(output_subdir, 'left.jpg')
    right_output_path = os.path.join(output_subdir, 'right.jpg')
    framed_output_path = os.path.join(output_subdir, 'framed.jpg')

    cv.imwrite(left_output_path, left_part)
    cv.imwrite(right_output_path, right_part)
    cv.imwrite(framed_output_path, framed)
