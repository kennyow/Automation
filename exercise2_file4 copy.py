from pathlib import Path
from datetime import datetime

root_dir = Path('Automation/files4')

for path in root_dir.glob("**/*"):

    if path.is_file():
        #Gel all the status from the file
        stats = root_dir.stat()

        #Get the seconds from the file when it was opened
        second_created = stats.st_ctime

        #Transform seconds_created into date
        date_created = datetime.fromtimestamp(second_created)

        #Transform date_created into a string
        date_created_str = date_created.strftime("%Y-%m-%d_%H_%M_%S")

        #Create filename
        new_filename = date_created_str + '-' + path.name

        new_filepath = path.with_name(new_filename)

        path.rename(new_filepath)


        print(stats)
        print(second_created)
        print(date_created)
        print(date_created_str)

'''Access teh files
for path in file_paths:
    if path.is_file():
        path_parts = path.parts
        print(path.parts)
        subfolders = path.parts[2:4]
        #print(subfolders)
        new_filename = '-'.join(subfolders) + '-' + path.name
        #print(new_filename)
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)'''