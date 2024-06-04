import sqlite3
import pandas as pd
import openpyxl


#Establish a connection and create cursos
path =  'Automation/sql_databases/'
con = sqlite3.connect(path+'database.db')

cur = con.cursor()

df = pd.read_sql_query("SELECT * FROM 'ips' ORDER BY asn", con)
print(df)

#CSV
df.to_csv(path+'database.csv', index=None) #Remove index

#EXCEL
df.to_excel(path+'database.xlsx', index=None) #Remove index
