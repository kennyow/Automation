#pip install opencv-python
import cv2

#0 = grayscale, 1 = color version
color = cv2.imread('Automation/image_processing/galaxy.jpeg', 1)
#ndim = number of dimensions
print(color.ndim)

color = cv2.imread('Automation/image_processing/galaxy.jpeg', 0)
cv2.imwrite('Automation/image_processing/galaxy-gray.jpeg', color)
