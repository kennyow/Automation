



path = 'Automation/text_processing/'

#First Way
file = open(path+'file1.txt', 'w')
file.write('Manchester United\n')
file.write('Santos')
file.close()

#Second Way
file = open(path+'file2.txt', 'w')
content = """
Manchester City
Liverpool
Arsenal
Chelsea
Tottenham
"""
file.write(content)
file.close()

#Third Way
with open(path+'file3.txt', 'w') as file:
    file.write('Sporting Crystal\n')
    file.write('Perilima')
