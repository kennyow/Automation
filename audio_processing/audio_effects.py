#pip install pydub
from pydub import AudioSegment


path = 'Automation/audio_processing/'

beat = AudioSegment.from_wav(path+'beat.wav')
beat_low = beat.low_pass_filter(2000)
beat_low.export(path+'beat_low.wav', format='wav')

beat_left = beat_low.pan(-1)
beat_left.export(path+'beat_left.wav', format='wav')

beat_right = beat_low.pan(1)
beat_right.export(path+'beat_right.wav', format='wav')

beat_final = beat_left + beat_right + beat_low
beat_final.export(path+'beat_final.wav', format='wav')

print(dir(AudioSegment))