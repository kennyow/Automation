import cv2


path = 'Automation/webcam_capture_video_processing/'

video = cv2.VideoCapture(path+"video.mp4")
success, frame = video.read() #Get the first frame

count = 1
while success:
    cv2.imwrite(f'{path}images/{count}.jpg', frame)
    success, frame = video.read()  #Get the second frame and so on
    count += 1
