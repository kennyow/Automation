#pip install tabula-py
import tabula

#archieve, number of the page
table = tabula.read_pdf('Automation/generate_pdf/Table+and+Text.pdf', pages=1)

print(type(table[0]))

#To not print the index
table[0].to_csv('Automation/generate_pdf/output2.csv', index=None)