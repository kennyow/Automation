from pathlib import Path

# It deletes all data inside the file
#a.txt has 'Manchester United' and b.txt has Arsenal
root_dir = Path('Automation/files9')

for path in root_dir.glob("*.txt"):
    with open(path, 'wb') as file:
        file.write(b'')