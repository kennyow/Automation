import yagmail
import os
import time

my_email = os.getenv('email')

#google app 2 step verification password
my_password = os.getenv('password')

print(my_email, my_password)
sender = my_email
receiver = 'kennyow86@gmail.com'

subject = 'EAE'
contents = """ 
We all have a weakness
Some of ours are easy to identify
Look me in the eye
And ask for forgiveness

We'll make a pact
To never speak that word again
Yes, you are my friend

We all have something that digs at us
At least we dig each other
So when weakness turns my ego up
I know you'll count on the me from yesterday

If I turn into another dig me up from under
What is covering the better part of me, sing this song
Remind me that we'll always have each other
When everything else is gone, oh

We all have a sickness
That cleverly attaches and multiplies
No matter how we try

We all have someone that digs at us
At least we dig each other
So when sickness turns my ego up
I know you'll act as a clever medicine

If I turn into another dig me up from under
What is covering the better part of me
Sing this song (sing this song)
Remind me that we'll always have each other
When everything else is gone

Oh, each other
When everything else is gone

If I turn into another dig me up from under
What is covering the better part of me
Sing this song (sing this song)
Remind me that we'll always have each other
When everything else is gone

Oh, each other (sing this song)
When everything else is gone
Oh, each other
When everything else is gone"""

while True:

    yag = yagmail.SMTP(user=my_email, password=my_password)
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")
    time.sleep(5)
