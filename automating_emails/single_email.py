#pip install yagmail
import yagmail
import os

my_email = os.getenv('email')

#google app 2 step verification password
my_password = os.getenv('password')

print(my_email, my_password)
sender = my_email
receiver = 'kennyow86@gmail.com'

subject = 'IAI'
contents = """ 
Sometimes I feel the fear
Of uncertainty stinging clear
And I can't help but ask myself how much
I'll let the fear take the wheel and steer

It's driven me before
And it seems to have a vague
Haunting mass appeal
But lately I'm beginning to find that
I should be the one behind the wheel

Whatever tomorrow brings I'll be there
With open arms and open eyes, yeah
Whatever tomorrow brings I'll be there
I'll be there

So if I decide to waiver my chance
To be one of the hive
Will I choose water over wine
And hold my own and drive? Oh, oh, oh

It's driven me before
And it seems to be the way
That everyone else gets around
But lately I'm beginning to find that
When I drive myself my light is found

Whatever tomorrow brings I'll be there
With open arms and open eyes, yeah
Whatever tomorrow brings I'll be there
I'll be there

Would you choose water over wine
Hold the wheel and drive

Whatever tomorrow brings I'll be there
With open arms and open eyes, yeah
Whatever tomorrow brings I'll be there
I'll be there

Do, do, do
Do, do, do
Do, do, do, do, do
No, no, no

Do, do, do, do, do
Do, do, do
Do, do, do
Do, do, do, do, do
No, no, no, no"""

yag = yagmail.SMTP(user=my_email, password=my_password)
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")
