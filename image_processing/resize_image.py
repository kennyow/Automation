import cv2


image = cv2.imread('Automation/image_processing/galaxy.jpeg')
path = 'Automation/image_processing/'
print(image.shape)

def calculate_size(scale_percentage, width, height):
    new_width = int(width * scale_percentage / 100)
    new_height = int(height * scale_percentage / 100)
    return (new_width, new_height)

#Scale Percentage, width, height
print(calculate_size(10, image.shape[1], image.shape[0]))

def resize(image_path, scale_percentage, resized_path):
    image = cv2.imread(image_path)
    new_dim = calculate_size(scale_percentage, image.shape[1], image.shape[0])
    resized_image = cv2.resize(image, new_dim)
    cv2.imwrite(resized_path, resized_image)


resize(path+'galaxy.jpeg', 10, path+'resized-galaxy.jpeg')