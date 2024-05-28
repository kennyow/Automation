import os
import cv2

images = os.listdir('Automation/image_processing/exercise1/images')
for image in images:
  print(image)
  gray = cv2.imread(f'Automation/image_processing/exercise1/images/{image}', 0)
  print(gray)
  cv2.imwrite(f'Automation/image_processing/exercise1/grey_images/gray-{image}', gray)

            