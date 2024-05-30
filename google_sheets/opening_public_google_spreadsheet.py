import pandas as pd

path = 'Automation/google_sheets/'

url_sheet1 = "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet=2013"
url_sheet2 = "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet=2014"
data1 = pd.read_csv(url_sheet1)
data2 = pd.read_csv(url_sheet2)

print(data1)
print(data2)