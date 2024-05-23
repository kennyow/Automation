from pathlib import Path
from datetime import datetime

root_dir = Path('Automation/files5')

#Creating empty files from 10 to 20

for i in range (10, 21):
    filename = str(i) + '.txt'
    #Create the path object
    filepath = root_dir/ Path(filename)
    filepath.touch()