#pip install sounddevice
#pip install scipy
import sounddevice
from scipy.io.wavfile import write

path = 'Automation/controling_devices/'

seconds = 5
fps = 44100

myrecording = sounddevice.rec(frames=seconds * fps, samplerate=fps, channels = 1)
sounddevice.wait()
write(path+'output.mp3', fps, myrecording)