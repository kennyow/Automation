import gspread
import statistics

# Authenticate and open the spreadsheet
path = 'Automation/google_sheets/'
gc = gspread.service_account(filename=path+'secrets.json')

spreadsheet = gc.open('Automation - Udemy')

# Get worksheet by name
worksheet1 = spreadsheet.worksheet('2013')

# Get values from column G (G2:G25)
existing_column = worksheet1.get_values('G2:G25')
print("Raw values from G2:G25:", existing_column)

# Flatten the existing column and handle non-numeric values
try:
    existing_column = [float(i[0].replace(',', '.')) for i in existing_column if i[0].strip() != '']
    print("Converted to floats:", existing_column)
except ValueError as e:
    print(f"Error converting values to float: {e}")

# Calculate average and add to Worksheet
if existing_column:
    average = statistics.mean(existing_column)
    print(f"Calculated average: {average}")
    worksheet1.update('G26', [[average]])  # Wrap the average in a list of lists
    print("Updated cell G26 with the average.")
else:
    print("No valid numeric values found in the specified range.")
