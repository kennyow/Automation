import gspread
import re #regular expressions

path = 'Automation/google_sheets/'
gc = gspread.service_account(path+'secrets.json')


spreadsheet = gc.open('Automation - Udemy')

#Get worksheet by name
worksheet1 = spreadsheet.worksheet('2013')

#Update a cell
worksheet1.update('E5', [[88]])

#Update a cell based on row-column
worksheet1.update_cell(5, 5, -39)