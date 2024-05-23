from pathlib import Path

p1 = Path('Automation/Computer_Files/ghi.txt')
print(type(p1))


if not p1.exists():   
    with open(p1, 'w') as file:
            file.write('Content 3')

print(p1.name)
print(p1.stem) #name without extension
print(p1.suffix) # format file


p2 = Path('Automation/Computer_Files')
print(list(p2.iterdir()))