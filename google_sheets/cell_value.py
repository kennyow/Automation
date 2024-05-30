import gspread
import re #regular expressions

path = 'Automation/google_sheets/'
gc = gspread.service_account(path+'secrets.json')


spreadsheet = gc.open('Automation - Udemy')

#Get worksheet by name
worksheet2 = spreadsheet.worksheet('2013')
print(worksheet2)

#Get cell value
data = worksheet2.get_values('D5')[0][0] #[0][0] is to get outside the lists
print(data)

#Get cell using acell 
data2 = worksheet2.acell('D5').value
print(data2)

#Search for a cell
data3 = worksheet2.find('-10')
print(data3.row, data3.col)


#Search for many cells
data4 = worksheet2.findall('-9')
for cell in data4:
    print(cell.row, cell.col)

#Values that starts with 99
reg = re.compile(r'99')
cells = worksheet2.findall(reg)

for cell in cells:
    print(cell.row, cell.col)