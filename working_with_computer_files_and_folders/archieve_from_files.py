from pathlib import Path
import zipfile


#Putting text files inside zip files and rar files
root_dir = Path('Automation/files6')

archive_path = root_dir/ Path('archive.zip')

with zipfile.ZipFile(archive_path, 'w') as zf:
    for path in root_dir.rglob("*.txt"):
        zf.write(path)
        path.unlink() #To delete files from the folder