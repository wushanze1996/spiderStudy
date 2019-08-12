import requests
from bs4 import BeautifulSoup
url='https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html'
res=requests.get(url)
html = res.text
soup=BeautifulSoup(html,"html.parser")
books = soup.find_all(class_="books")
for book in books:
    kind= book.find('h2').text
    title =book.find(class_="title")
    href = title['href']
    print(kind+'\n'+title.text+'\n'+href+'\n')