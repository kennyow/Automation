import gspread


path = 'Automation/google_sheets/'
gc = gspread.service_account(path+'secrets.json')


spreadsheet = gc.open('Automation - Udemy')

#Get a worksheet by index
worksheet1 = spreadsheet.get_worksheet(0)
print(worksheet1)

#Get the data
data = worksheet1.get_all_records()
#print(data)

#Get the tenth row (it jumps the first row with column names)
#print(data[0])

#Get worksheet by name
worksheet2 = spreadsheet.worksheet('2013')
print(worksheet2)