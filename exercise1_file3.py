from pathlib import Path


root_dir = Path('Automation/files3')
file_paths = root_dir.glob("**/*") #list

#Access teh files
for path in file_paths:
    if path.is_file():
        path_parts = path.parts
        print(path.parts)
        subfolders = path.parts[2:4]
        #print(subfolders)
        new_filename = '-'.join(subfolders) + '-' + path.name
        #print(new_filename)
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)