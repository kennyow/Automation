from pathlib import Path


path = 'Automation/text_processing/'
files_dir = Path(path+'files')


merged=''
for index, filepath in enumerate (files_dir.iterdir()):
    with open(filepath, 'r') as file:
        content = file.readlines()
        new_content = content[1:]
    if index ==0:
        content = ''.join(content)
        merged += content + '\n'
    else:
        new_content = ''.join(new_content)
        merged += new_content + '\n'


with open(path+'merged-supernew.csv', 'w') as file:
    file.write(merged)
