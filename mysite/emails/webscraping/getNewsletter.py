import requests
from bs4 import BeautifulSoup
import pprint

# Path: mysite\emails\webscraping\getNewsletter.py
#find the newsletter div

def get_newsletter():
    URL = "https://techcrunch.com/category/cryptocurrency/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    # results are in a h2 class called post-block__title
    results = soup.find_all('h2', class_='post-block__title')
    links = []
    titles = []
    for result in results:
        link = result.find('a')  
        links.append(link['href'])
        title = result.find('a').text.strip()
        titles.append(title)  
    return links, titles


get_newsletter()




