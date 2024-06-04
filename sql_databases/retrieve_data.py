import sqlite3


#Establish a connection and create cursos
path =  'Automation/sql_databases/'
con = sqlite3.connect(path+'database.db')

cur = con.cursor()

#Execute SQL getting all rows and columns by order
cur.execute("SELECT * FROM 'ips' ORDER BY asn")
print(cur.fetchall())

#Getting all rows and certain columns
cur.execute("SELECT address, asn FROM 'ips' ORDER BY asn")
print(cur.fetchall())

#Get all rows where asn is less than 300
cur.execute("SELECT * FROM 'ips' WHERE asn < 300")
print(cur.fetchall())

#Get all rows where asn is 144
cur.execute("SELECT * FROM 'ips' WHERE asn = 144")
print(cur.fetchall())

#Get all rows where asn is 144
cur.execute("SELECT * FROM 'ips' WHERE asn < 300 AND domain LIKE '%sa'")
print(cur.fetchall())