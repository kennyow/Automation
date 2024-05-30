import gspread
from time import sleep

# Authenticate and open the spreadsheet
path = 'Automation/google_sheets/'
gc = gspread.service_account(filename=path+'secrets.json')

spreadsheet = gc.open('Automation - Udemy')

# Get worksheet by name
worksheet1 = spreadsheet.worksheet('2013')
worksheet2 = spreadsheet.worksheet('Watch')


while True:
    value1 = worksheet1.acell('G26').value
    sleep(2)
    value2 = worksheet1.acell('G26').value
    if value1 != value2:
        worksheet2.update('A1', [['CHANGED']])