from pathlib import Path
import rarfile
#import zipfile

# Putting text files inside RAR files
root_dir = Path('Automation/files7')
destination_path = Path('Automation/destination')

for path in root_dir.rglob("*.rar"): #.zip
    with rarfile.RarFile(path, 'r') as rf:
        final_path = destination_path / Path(path.stem)
        rf.extractall(path=final_path)