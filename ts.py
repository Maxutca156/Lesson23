import requests
from bs4 import BeautifulSoup

url = 'https://dedmorozural.ru/'
response = requests.get(url)
print(response.status_code)
print(response.text)

soup = BeautifulSoup(response.text, features='html.parser')
print(type(soup.title))

print(soup.a)
print(soup.a.string)
print(soup.a.get('href'))

images_tags = soup.find_all('img')
for images_tags in images_tags:
    print(images_tags)

a_tags = soup.find_all('a')
for a_tags in a_tags:
    print(a_tags)

big_body_div = soup.find(name='div', class_='modulebody1')

print(big_body_div)
