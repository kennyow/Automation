import cv2
import os
import numpy as np

columns = 3
rows = 2
path = 'Automation/image_processing/'

horizontal_margin = 40
vertical_margin = 20

images = os.listdir(os.path.join(path, 'images'))
image_objects = [cv2.imread(os.path.join(path, 'images', filename)) for filename in images]
print(images)

# Ensure that the first image exists and get its shape
first_image_path = os.path.join(path, 'images', '1.jpeg')
first_image = cv2.imread(first_image_path)
if first_image is None:
    raise ValueError(f"Failed to load image at {first_image_path}")

shape = first_image.shape
print(shape)

big_image = np.zeros((shape[0] * rows + horizontal_margin * (rows + 1),
                      shape[1] * columns + vertical_margin * (columns + 1),
                      shape[2]), np.uint8)

big_image.fill(255)

positions = [(x, y) for y in range(rows) for x in range(columns)]
print(positions)

for (pos_x, pos_y), image in zip(positions, image_objects):
    x = pos_x * (shape[1] + vertical_margin) + vertical_margin
    y = pos_y * (shape[0] + horizontal_margin) + horizontal_margin
    big_image[y:y+shape[0], x:x+shape[1]] = image

cv2.imwrite(os.path.join(path, 'grid.jpeg'), big_image)
