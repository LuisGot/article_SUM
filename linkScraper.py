import requests
from bs4 import BeautifulSoup

def get_urls_from_futuretools():

    futuretools = requests.get("https://www.futuretools.io/news").text
    soup = BeautifulSoup(futuretools, 'html.parser')

    urls = []

    for url in soup.find_all('a', {'href': True}):
        if url.find_parent("div", {"role": "listitem"}):
            urls.append(url.get('href'))

    return urls


