import cv2
import os

path = 'Automation/image_processing/exercise2/'

def calculate_size(scale_percentage, width, height):
    new_width = int(width * scale_percentage / 100)
    new_height = int(height * scale_percentage / 100)
    return (new_width, new_height)

def resize(image_path, scale_percentage, resized_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load image at {image_path}")
        return
    new_dim = calculate_size(scale_percentage, image.shape[1], image.shape[0])
    resized_image = cv2.resize(image, new_dim)
    cv2.imwrite(resized_path, resized_image)

images_path = os.path.join(path, 'images')
print(images_path)
resized_images_path = os.path.join(path, 'resized_images')

# Ensure the resized_images directory exists
os.makedirs(resized_images_path, exist_ok=True)

images = os.listdir(images_path)
#print(images)

for image in images:
    image_path = os.path.join(images_path, image)
    resized_image_path = os.path.join(resized_images_path, f"resized-{image}")
    resize(image_path, 10, resized_image_path)
