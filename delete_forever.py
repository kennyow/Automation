from pathlib import Path

root_dir = Path('Automation/files9')

for path in root_dir.glob("*.txt"):
    with open(path, 'wb') as file:
        file.write(b'')