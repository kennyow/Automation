import cv2


path = 'Automation/webcam_capture_video_processing/'
video = cv2.VideoCapture(path+"video.mp4")

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
n_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(video.get(cv2.CAP_PROP_FPS))

print(width, height, n_frames, fps)
