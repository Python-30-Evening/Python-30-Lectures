""" Parsing and Web Scraping """

# Parsing - фильтрация данных из кучи данных
# Web Scraping - получение данных с интернета

from bs4 import BeautifulSoup

with open('index.html', 'r') as html:
    html_code = html.read()
    # print(html_code)

soup = BeautifulSoup(html_code, 'html.parser')
title = soup.find('title')
# print(title.text)
# divs = soup.find_all('div')
# print(divs)
div2 = soup.find('div', class_='div2')
img = div2.find('img')
print(img.get('src'))
