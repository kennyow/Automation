from pathlib import Path

#Replacing amounts for units on each csv file
path = 'Automation/text_processing/'
files_dir = Path(path+'files')

for filepath in files_dir.iterdir():
    with open(filepath, 'r') as file:
        content = file.read()
        new_content = content.replace('amount', 'units')
    
    with open(filepath, 'w') as file:
        file.write(new_content)
        
