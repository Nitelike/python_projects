import requests
from bs4 import BeautifulSoup

search = input('Введите тему: ')
url = 'https://www.google.com/search?q=' + search
headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36,gzip(gfe)'}

def parse(url, headers):
    session = requests.Session()
    request = session.get(url, headers=headers)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'r'})
        hrefs = []
        content = []
        for div in divs:
            hrefs.append(div.find('a', recursive=False)['href'])

        for href in hrefs:
            page_request = session.get(href, headers=headers)
            page_soup = BeautifulSoup(page_request.content, 'html.parser')
            p = page_soup.find_all('p')
            for p_text in p:
                text = p_text.text
                text = text.replace('\n', '')
                text = text.replace('\r', '')
                text = text.replace('\t', '')
                content.append(text)

        with open(search + '.txt', 'w', encoding="utf-8") as output:
            output.write(' '.join(content))

        print('Сохранено в файле ' + search + '.txt')
    else:
        print('ERROR')

parse(url, headers)