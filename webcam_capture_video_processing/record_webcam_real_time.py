import cv2

path = 'Automation/webcam_capture_video_processing/'

#0 corresponds to the Webcam
video = cv2.VideoCapture(0)
success, frame = video.read() #Get the first frame

#Dimensions of the original video
height = frame.shape[0]
width = frame.shape[1]

face_cascade = cv2.CascadeClassifier(path+'faces.xml')
output = cv2.VideoWriter(path+'output.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

count = 0
while success:
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x, y , w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,255), 4)
    cv2.imshow('Recording', frame)
    key = cv2.waitKey(1) #milisseconds
    if key == ord('q'): #press q to quit
        break
    output.write(frame)
    success, frame = video.read()  #Get the second frame and so on
    count += 1
    print(count) #Count the frames
output.release()
video.release()
cv2.destroyAllWindows()