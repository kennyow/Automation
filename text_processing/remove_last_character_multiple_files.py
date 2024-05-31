from pathlib import Path


path = 'Automation/text_processing/'
files_dir = Path(path+'files')

for filepath in files_dir.iterdir():
    with open(filepath, 'r') as file:
        content = file.read()
        new_content = content[:-1]
        
    with open(filepath, 'w') as file:
        file.write(new_content)
