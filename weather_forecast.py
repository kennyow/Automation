import requests



def get_weather(city, units='metric', api_key = '56c91a4840c19a1c02cebc5078d2a8ed'):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}'
    r = requests.get(url)
    content = r.json()
    with open('data.txt', 'a') as file:
        for dicty in content['list']:
            file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")
    


print(get_weather(city='Miami'))