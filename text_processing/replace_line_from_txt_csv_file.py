from pathlib import Path


path = 'Automation/text_processing/'


with open(path+'merged.csv', 'r') as file:
    content = file.readlines()

content[0] = 'ID,AMOUNT,COST\n'

with open(path+'merged.csv', 'w') as file:
    file.writelines(content)