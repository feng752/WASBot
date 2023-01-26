import requests
from bs4 import BeautifulSoup


tips_and_resources = []

# Define the websites to scrape
websites = [
    'https://www.gamedeveloper.com/latest/news',
    'https://gamedev.expert/category/news/',
    'https://www.polygon.com/gaming'
]  # TODO implement general checking


# Make the request and parse the HTML
def scraper():
    for url in websites:
        response = requests.get(url)
        html = response.content

        soup = BeautifulSoup(html, 'html.parser')

        if "gamedeveloper" in url:  # Different HTML structures for each website
            articles = soup.find_all('div', class_='topic-content-article')
            for article in articles:
                title = article.find('span', class_='article-title').text
                link = article.find('a')['href']
                tips_and_resources.append({'title': title, 'link': 'https://gamedeveloper.com' + link})

        elif "gamedev.expert" in url:
            articles = soup.find_all('h2', class_='title')
            for article in articles:
                title = article.find('a').text
                link = article.find('a')['href']
                tips_and_resources.insert(0, {'title': title, 'link': link})

        elif "polygon" in url:
            articles = soup.find_all('h2', class_='c-entry-box--compact__title')
            for article in articles:
                title = article.find('a').text
                link = article.find('a')['href']
                tips_and_resources.insert(0, {'title': title, 'link': link})


scraper()

for item in tips_and_resources:
    print("Title: " + item['title'])
    print("\nLink: " + item['link'] + "\n")
