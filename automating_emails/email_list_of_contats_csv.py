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

subject = 'EAAAE'


#Login
yag = yagmail.SMTP(user=my_email, password=my_password)


#Creating DataFrame
df = pd.read_csv("Automation/automating_emails/contacts.csv")
print(df)

#Iterate through
for index, row in df.iterrows():
    while True:
        now = dt.now()
        if now.hour == 10 and now.minute == 3:
            contents = f"""
                Hi, {row['name']}, o majestoso poderoso! Bora cantar!

                I dig my toes into the sand
                The ocean looks like a thousand diamonds
                Strewn across a blue blanket
                I lean against the wind
                Pretend that I am weightless
                And in this moment I am happy
                Happy

                I wish you were here
                I wish you were here
                I wish you were here
                I wish you were here

                I lay my head onto the sand
                The sky resembles a back-lit canopy
                With holes punched in it
                I'm counting UFOs
                I signal them with my lighter
                And in this moment I am happy
                Happy

                I wish you were here
                I wish you were here
                I wish you were here
                Wish you were here

                The world's a roller coaster
                And I am not strapped in
                Maybe I should hold with care
                But my hands are busy in the air saying

                I wish you were here
                I wish you were
                I wish you were here
                I wish you were here
                I wish you were here
                Wish you were here"""
            yag.send(to=row['email'], subject=subject, contents=contents)
            print("Email Sent!")
            time.sleep(5)
