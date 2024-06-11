import cv2 as cv2


path = 'Automation/face_censoring/'
video = cv2.VideoCapture(path+'smile.mp4')

success, frame = video.read()
height = frame.shape[0]
width = frame.shape[1]

face_cascade = cv2.CascadeClassifier(path+'faces.xml')


output = cv2.VideoWriter(path+'blurred_smile.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

count = 0
while success:
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x, y, w, h) in faces:
        frame[y:y+h, x:x+w] = cv2.blur(frame[y:y+h, x:x+w], (50, 50))
    output.write(frame)
    success, frame = video.read()
    count += 1
    
output.release()