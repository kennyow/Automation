import yagmail
import os
import time
from datetime import datetime as dt
import pandas as pd

my_email = os.getenv('email')

#google app 2 step verification password
my_password = os.getenv('password')

sender = my_email
receiver = 'kennyow86@gmail.com'

subject = 'CHORA NO BOY'




#Creating DataFrame
df = pd.read_csv("Automation/automating_emails/contacts.csv")
#print(df)

#Iterate through
for index, row in df.iterrows():
    while True:
        now = dt.now()
        if now.hour == 10 and now.minute == 45:
            contents = ["""
                Hi, {row['name']}, o majestoso poderoso! Bora cantar!

                Oh, stellar
                Meet me in outer space
                We could spend the night
                Watch the earth come up
                I've grown tired of that place
                Won't you come with me?
                We could start again

                How do you do it?
                Make me feel like I do
                How do you do it?
                It's better than I ever knew

                Meet me in outer space
                I will hold you close
                If you're afraid of heights
                I need you to see this place
                It might be the only way
                That I can show you how
                It feels to be inside of you

                How do you do it?
                Make me feel like I do
                How do you do it?
                It's better than I ever knew

                You are stellar
                You are stellar

                How do you do it?
                Make me feel like I do
                How do you do it?
                It's better than I ever knew""", 'email_with_attachment.txt']
            #Login
            yag = yagmail.SMTP(user=my_email, password=my_password)
            yag.send(to=row['email'], subject=subject, contents=contents)
            print("Email Sent!")
            time.sleep(5)
