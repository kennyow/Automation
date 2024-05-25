#pip install PyMuPDF
import fitz

with fitz.open('Automation/generate_pdf/students.pdf') as pdf:
    for page in pdf:
        print(50* '-')
        print(page.get_text())

# First page only:
# with fitz.open('Automation/generate_pdf/students.pdf') as pdf:
#     page1 = pdf[0.get_text()] in pdf:
#     print(page1)

#Get all the text pages into a single text
# with fitz.open('Automation/generate_pdf/students.pdf') as pdf:
#     text = ''
#     for page in pdf:
#         text += page.get_text()
#         print(text)