path = 'Automation/text_processing/'


with open(path+'file3.csv', 'r') as file:
    content = file.read()

#Show everything but the last character
modified_content = content[:-1]

with open(path+'file-novo.csv', 'w') as file:
    file.write(modified_content)
