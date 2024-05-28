import cv2
import os

CASCADE = 'Automation/image_processing/faces.xml'
INPUT_FOLDER = 'Automation/image_processing/exercise3/input'
OUTPUT_FOLDER = 'Automation/image_processing/exercise3/output'
COLOR = (255,255,255)
WIDTH = 4
SCALE = 1.1
NEIGHBORS = 4

def has_face(image_path):
    image = cv2.imread(image_path, 1)
    face_cascade = cv2.CascadeClassifier(CASCADE)

    #All sizes of faces. 1.1 - increase de scale, 4 - minimum neighbours
    faces = face_cascade.detectMultiScale(image, SCALE, NEIGHBORS)
    print(faces)
    if len(faces) != 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x,y), (x+w, y+h), COLOR, WIDTH)
    return image

images = os.listdir(INPUT_FOLDER)
for image_path in images:
    print(image_path)
    face_image =  has_face(f'{INPUT_FOLDER}/{image_path}')
    if face_image is not None:
        cv2.imwrite(f'{OUTPUT_FOLDER}/{image_path}', face_image)

