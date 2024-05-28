import cv2
import numpy as np


path = 'Automation/image_processing/'
foreground = cv2.imread(path+'giraffe.jpeg')
background = cv2.imread(path+'safari.jpeg')

width = foreground.shape[1]
height= foreground.shape[0]

resized_background = cv2.resize(background, (width, height))

for i in range(width):
    for j in range (height):
        pixel = foreground[j,i]
        if np.any(pixel == [1, 255, 0]): #Green pixel
            foreground[j, i] = resized_background[j,i]

cv2.imwrite(path+'output_foreground.jpeg', foreground)