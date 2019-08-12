import requests
from bs4 import BeautifulSoup
url = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html,'html.parser')
books = soup.find_all('article',class_="product_pod")
for book in books:
    h3 = book.find('h3')
    a = h3.find('a')
    print(a.text)
