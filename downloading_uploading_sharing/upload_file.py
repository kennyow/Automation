import requests

#from https://cgi-lib.berkeley.edu/ex/fup.html
url = "https://cgi-lib.berkeley.edu/ex/fup.cgi"
path = 'Automation/downloading_uploading_sharing/'


file = open(path+'myfile.txt', 'rb')

req = requests.post(url, files={"upfile":file})

print(req.text)