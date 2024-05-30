#Get the A5 to F5 on google sheet

import gspread


path = 'Automation/google_sheets/'
gc = gspread.service_account(path+'secrets.json')


spreadsheet = gc.open('Automation - Udemy')

#Get worksheet by name
worksheet2 = spreadsheet.worksheet('2013')
print(worksheet2)

data = worksheet2.get_values('A5:F5')
print(data)

#Get more than 1 row
data1 = worksheet2.get_values('A5:F7')
print(data1)

#Get an entire column without the header
data2 = worksheet2.get_values('C2:C25')
print(data2)

#Get all the values from the second column
data3 = worksheet2.col_values(2)
print(data3)