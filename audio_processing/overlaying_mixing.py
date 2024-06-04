#pip install pydub
from pydub import AudioSegment


path = 'Automation/audio_processing/'

beat = AudioSegment.from_wav(path+'beat.wav')
sax= AudioSegment.from_wav(path+'sax.wav')

# Different length
print(len(beat), len(sax))

beat10 = beat * 2
beat10.export(path+'beat10.wav', format="wav")

mixed = beat10.overlay(sax)
mixed.export(path+'mixed2.wav', format="wav")

final = beat10 + mixed * 2 + sax + beat10 + sax
final.export(path+'mixed3.wav', format="wav")