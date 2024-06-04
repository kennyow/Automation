from speech_recognition import Recognizer, AudioFile



path = 'Automation/audio_processing/'
recognizer = Recognizer()


with AudioFile(path+'chile.wav') as audio_file:
    audio = recognizer.record(audio_file)

text = recognizer.recognize_google(audio)
print(text)