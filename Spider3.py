import requests
from bs4 import BeautifulSoup
url = 'http://www.xiachufang.com/explore/'
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html,'html.parser')
list_foods  =  soup.find_all('div',class_="info pure-u")
list_a=[]



for food in list_foods:
    info = food.find('a')
    one = food.find('p',class_="ing ellipsis")
    name = info.text[17:-13]
    detail = one.text[1:-1]
    URL = 'http://www.xiachufang.com'+info['href']
    list_a.append([name,detail,URL])
for food in list_a:
    print(food)



