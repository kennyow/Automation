#pip install SpeechRecognition
from speech_recognition import Recognizer, AudioFile
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

recognizer = Recognizer()
path = 'Automation/finding_mood/'

with AudioFile(path+'chile.wav') as audio_file:
    audio = recognizer.record(audio_file)


text = recognizer.recognize_google(audio)

nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores(text)
print(scores)


if scores['compound'] > 0:
    print('Positive Speech')
else:
    print('Negative Speech')



