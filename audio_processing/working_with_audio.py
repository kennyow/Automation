#pip install pydub
from pydub import AudioSegment


path = 'Automation/audio_processing/'

original = AudioSegment.from_wav(path+'beat.wav')

print(original)

reversed = original.reverse()
reversed.export(path+'reversed.wav', format="wav")
reversed += 15 #High volume

#Methods
print(dir(original))

# first_two = original[0:2000] #milliseconds
# first_two.export(path+'first_two.wav', format="wav")

#Merge two audio files
merged = original * 2 + AudioSegment.silent(1000) + reversed #1000 milliseconds = 1 second
merged.export(path+'merged.wav', format="wav")