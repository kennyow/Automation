from pathlib import Path

#path = Path('Automation/files8/Items1/13.txt')

#Gives the entire path since the origin
#print(path.absolute())

root_dir = Path('Automation/files8')
search_term = '14'

for path in root_dir.rglob("*"):
    if search_term in path.stem:
        print(path.absolute())
