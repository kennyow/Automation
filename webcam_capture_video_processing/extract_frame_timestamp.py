import cv2

path = 'Automation/webcam_capture_video_processing/'

video = cv2.VideoCapture(path+"video.mp4")


n_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAP_PROP_FPS)

#print(n_frames, fps)

timestamp = '00:00:02.75'

timestamp_list = timestamp.split(':')
#print(timestamp_list)
timestamp_list_floats = [float(i) for i in timestamp_list]
hours, minutes, seconds = timestamp_list_floats
#print(hours, minutes, seconds)

frame_n = hours * 3600 * fps + minutes * 60 * fps + seconds * fps

video.set(1, frame_n)

success, frame = video.read()
cv2.imwrite(f"{path}Frame_at_{hours}_{minutes}_{seconds}.jpg", frame)