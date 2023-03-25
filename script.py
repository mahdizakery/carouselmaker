import os
import sys
import cv2 as cv
import numpy as np

# Get the directory path from the command line arguments, or use the script directory as default
if len(sys.argv) > 1:
    input_dir = sys.argv[1]
else:
    input_dir = os.path.dirname(os.path.abspath(__file__))

# Create the output directory if it doesn't exist
output_dir = os.path.join(input_dir, "output_images")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process all image files in the input directory
for file_name in os.listdir(input_dir):
    # Check if the file is an image
    if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        # Load the image
        img_path = os.path.join(input_dir, file_name)
        img = cv.imread(img_path)

        # Slice the image
        height, width, color = img.shape
        frame_width = np.ceil(width / 2).astype(int)
        left_part = img[:, :frame_width]
        right_part = img[:, frame_width:]

        # Create the framed image
        scale = 49
        w = int(img.shape[1] * scale / 100)
        h = int(img.shape[0] * scale / 100)
        dim = (w, h)
        resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
        h_resized, w_resized, _ = resized.shape

        framed = np.zeros((height, frame_width, 3), np.uint8)
        framed[:, :] = (255, 255, 255)
        x_center = int(framed.shape[1] / 2 - w_resized / 2)
        y_center = int(framed.shape[0] / 2 - h_resized / 2)
        framed[y_center:y_center + h_resized, x_center:x_center + w_resized] = resized

        # Create the output subdirectory if it doesn't exist
        output_subdir = os.path.join(output_dir, os.path.splitext(file_name)[0])
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        # Save the left, right, and framed images
        cv.imwrite(os.path.join(output_subdir, "left.jpg"), left_part)
        cv.imwrite(os.path.join(output_subdir, "right.jpg"), right_part)
        cv.imwrite(os.path.join(output_subdir, "framed.jpg"), framed)
