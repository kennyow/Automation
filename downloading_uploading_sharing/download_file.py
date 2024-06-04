import requests

#from https://filesamples.com/formats/mp3
url = 'https://filesamples.com/samples/audio/mp3/Symphony%20No.6%20(1st%20movement).mp3'


path = 'Automation/downloading_uploading_sharing/'

req = requests.get(url)
content = req.content



with open(path + 'download.mp3', 'wb') as file:
    file.write(content)