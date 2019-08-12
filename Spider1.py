import requests
from bs4 import BeautifulSoup
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spder-men0.0.html')
html = res.text
soup = BeautifulSoup(html,'html.parser')
soup.find_all('div',class_='books')