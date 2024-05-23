import requests

'''r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2024-5-10&to=2024-5-15&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')

content = r.json()
print(content['articles'][0]['title']) # Grab only the articles from dictionary
print('-' * 50)
print(content['articles'][0]['description']) # Grab only the description from dictionary

articles = content['articles']

for article in articles: 
    print('TITLE\n', article['title'], '\nDESCRIPTION\n', article['description'])'''




def get_news (topic, from_date, to_date, language = 'en',
              api_key = '0cb6bbd15c2d415ebba7f533b337b159'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles: 
        results.append(f"TITLE\n', {article['title']}, '\nDESCRIPTION\n', {article['description']}")
    
    return results


print(get_news(topic='space', from_date= '2024-5-10', to_date='2024-5-15'))