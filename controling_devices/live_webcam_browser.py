import cv2
from flask import Flask, render_template, Response

video = cv2.VideoCapture(0)

def get_frame():
    while True:
        success, frame = video.read()
        if not success:
            break
        _, encoded_image = cv2.imencode('.jpg', frame)
        frame = encoded_image.tobytes()  # Corrected this line
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed_url')  # Corrected this line
def video_feed():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    try:
        app.run(debug=True)
    finally:
        video.release()  # Ensure video is released when app stops
