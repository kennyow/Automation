import yagmail
import os
import time
from datetime import datetime as dt

my_email = os.getenv('email')

#google app 2 step verification password
my_password = os.getenv('password')

sender = my_email
receiver = 'kennyow86@gmail.com'

subject = 'EAE'
contents = """ 
Tonight we drink to youth and holding fast to truth
I don't want to lose what I had as a boy
My heart still has a beat but love is now a feat
As common as a cold day in LA

Sometimes when I'm alone, I wonder
Is there a spell that I am under
Keeping me from seeing the real thing?

Love hurts but sometimes it's a good hurt
And it feels like I'm alive
Love sings when it transcends the bad things
Have a heart and try me
'Cause without love I won't survive

I'm fettered and abused, I stand naked and accused
Should I surface this one man submarine?
I only want the truth so tonight we drink to youth
I'll never lose what I had as a boy

Sometimes when I'm alone, I wonder
Is there a spell that I am under
Keeping me from seeing the real thing?

Love hurts but sometimes it's a good hurt
And it feels like I'm alive
Love sings when it transcends the bad things
Have a heart and try me
'Cause without love I won't survive"""

while True:
    now = dt.now()
    if now.hour == 9 and now.minute == 18:
        yag = yagmail.SMTP(user=my_email, password=my_password)
        yag.send(to=receiver, subject=subject, contents=contents)
        print("Email Sent!")
        time.sleep(5)
