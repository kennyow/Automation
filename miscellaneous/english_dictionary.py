import json


path =  'Automation/miscellaneous/'

file = open(path+'data.json')
data = json.load(file)


def define(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return None
    

word = input('Please enter a word: ')
definition = define(word)
if definition:
    for item in definition:    
        print(f'\033[93m{item}\033[0m]')
else:
    print('Word was not found!')