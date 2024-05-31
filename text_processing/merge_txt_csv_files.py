from pathlib import Path


path = 'Automation/text_processing/'
files_dir = Path(path+'files')


merged=''
for filepath in files_dir.iterdir():
    with open(filepath, 'r') as file:
        content = file.read()
    merged += content + '\n'


with open(path+'merged.csv', 'w') as file:
    file.write(merged)
