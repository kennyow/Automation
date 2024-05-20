from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  # Get the access to the source code of the page = requests
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find("span", class_="ccOutputRslt").get_text()
  rate = rate[0:-4]
  print(rate)

get_currency('EUR', 'AUD')

'''ticker = input("Enter the ticker symbol: ")
from_date = input ('Enter the start date in yyyy/mm/dd: ')
to_date = input ('Enter the end date in yyyy/mm/dd: ')

from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))

#The link below has the company name (AALP), the start and the finished period in seconds and the interval (1 day)

#F12 - Network - (big number) - scroll down to User-Agent
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

content = requests.get(url, headers=headers).content
print(content)

with open('data.csv', 'wb') as file:
  file.write(content)'''