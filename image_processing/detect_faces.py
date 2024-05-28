import cv2

path = 'Automation/image_processing/'

#image = cv2.imread(path+'humans.jpeg', 1)
image = cv2.imread(path+'chelsea.jpg', 1)
face_cascade = cv2.CascadeClassifier(path+'faces.xml')

#All sizes of faces. 1.1 - increase de scale, 4 - minimum neighbours
faces = face_cascade.detectMultiScale(image, 1.1, 4)

#List of lists with coordinates of retangles
#print(faces)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (255,255,255), 4)

cv2.imwrite(path+'chelsea_faces.jpeg', image)