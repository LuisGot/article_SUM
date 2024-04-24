import requests
from bs4 import BeautifulSoup


def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f'Ein Fehler ist aufgetreten: {e}')
        return None


def scrape_page(url):
    page_content = get_page_content(url)
    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')
        paragraphs = soup.find_all('p')
        content = ''
        for paragraph in paragraphs:
            content += paragraph.text + "\n\n"
        return content


