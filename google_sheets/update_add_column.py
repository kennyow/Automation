# convert into Fahrenheit
import gspread
import re #regular expressions

path = 'Automation/google_sheets/'
gc = gspread.service_account(path+'secrets.json')


spreadsheet = gc.open('Automation - Udemy')

#Get worksheet by name
worksheet1 = spreadsheet.worksheet('2013')

existing_column = worksheet1.get_values('E2:E25')
new_column = [[round((float(i[0]) * 9/5 + 32), 1)] for i in existing_column]
print(new_column)

#Creating a new column with converted values
worksheet1.update('G1:G25', [['Fahrenheit']]+new_column)