import requests
from bs4 import BeautifulSoup, Tag


url = 'https://max.kg/catalog/komputery-i-noutbuki-planshety/noutbuki'

response = requests.get(url)
if response.status_code == 200:
    html = response.text
else:
    raise Exception('Сайт не отвечает')

soup = BeautifulSoup(html, 'html.parser')

cards = soup.find_all('div', {'class': 'show-product-content'})

result = []
card: Tag
for card in cards:
    data = {
        'title': card.find('div', {'class': 'product-title'}).text,
        'price': card.find('span', {'class': 'sum-price'}).text,
        'link': card.find('div', {'class': 'product-title'}).find('a').get('href'),
        'image': card.find('img').get('src'),
    }
    result.append(data)

print(result)  # список из словарей


"""
1. Получить html
2. Превратить html в суп (soup)
3. Получить из супа карточки
4. Из каждой карточки отфильтровать нужные данные
5. Записать данные в файл
"""


# TODO: записать этот список в json файл
