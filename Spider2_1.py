import requests
from bs4 import BeautifulSoup
url = 'https://wordpress-edu-3autumn.localprod.forc.work/all-about-the-future_04/'
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html,'html.parser')
answers = soup.find_all('div',class_="comment-content")
for answer in answers:
    print(answer.text)
    with open('log.txt','a',encoding='utf-8') as f:
        f.write(answer.text)
    