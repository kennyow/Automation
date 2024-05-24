import yagmail
import os
import time
from datetime import datetime as dt
import pandas as pd

# Obter as credenciais do ambiente
my_email = os.getenv('email')
my_password = os.getenv('password')

# Login no yagmail
yag = yagmail.SMTP(user=my_email, password=my_password)

# Criar DataFrame a partir do arquivo CSV
df = pd.read_csv("Automation/automating_emails/contacts.csv")

def generate_file(filename, content):
    with open(filename, 'w') as file:
        file.write(str(content))

# Iterar sobre o DataFrame
for index, row in df.iterrows():
    name = row['name']
    filename = name + '.txt'
    amount = row['amount']
    receiver_email = row['email']

    # Diretório onde os arquivos serão salvos
    directory = "Automation/automating_emails"
    filepath = os.path.join(directory, filename)

    # Garantir que o diretório existe
    os.makedirs(directory, exist_ok=True)

    # Gerar o arquivo
    generate_file(filepath, amount)

    subject = 'Um dia qualquer em EZPERANZA'
    contents = [
        f"""
        Hi, {name}, o majestoso poderoso! Bora cantar!
        
        Tu tem que pagar {amount}!!
        """,
        filepath
    ]
    
    # Enviar o e-mail
    yag.send(to=receiver_email, subject=subject, contents=contents)
    print(f"Email Sent to {receiver_email} with attachment {filepath}!")
