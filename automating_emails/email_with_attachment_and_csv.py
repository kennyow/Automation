import yagmail
import os
import time
from datetime import datetime as dt
import pandas as pd

my_email = os.getenv('email')

#google app 2 step verification password
my_password = os.getenv('password')

sender = my_email
#receiver = 'kennyow86@gmail.com'


#Creating DataFrame
df = pd.read_csv("Automation/automating_emails/contacts.csv")
#print(df)

#Iterate through
for index, row in df.iterrows():
    while True:
        now = dt.now()
        if now.hour == 11 and now.minute == 22:
            receiver_email = row['email']
            subject = 'Chora Menina'
            contents = [f"""
                Hi, {row['name']}, o majestoso poderoso! Bora cantar!

                You are stellar
                You are stellar

                How do you do it?
                Make me feel like I do
                How do you do it?
                It's better than I ever knew
                
                Tu tem que pagar {row['amount']}!!
                """, f"Automation/automating_emails/{row['name']}"]
            #Login
            yag = yagmail.SMTP(user=my_email, password=my_password)
            yag.send(to=row['email'], subject=subject, contents=contents)
            print("Email Sent!")
            time.sleep(5)
