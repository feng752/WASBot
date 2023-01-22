import requests
from bs4 import BeautifulSoup


tips_and_resources = []

# Define the URL to scrape
url = 'https://www.gamedeveloper.com/latest/news'

# Make the request and parse the HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the article elements on the page
articles = soup.find_all('div', class_='topic-content-article')

# Iterate through the articles and extract the information we want
for article in articles:
    title = article.find('span', class_='article-title').text
    link = article.find('a')['href']
    tips_and_resources.append({'title': title, 'link': 'gamedeveloper.com' + link})

# Print the list of articles
for item in tips_and_resources:
    print("Title: " + item["title"])
    print("Link: " + item["link"])
    print("\n")

