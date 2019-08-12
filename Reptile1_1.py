import requests
from bs4 import BeautifulSoup
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')

unit =  res.text
num = res.status_code
twice = res.content
print(unit[:800])
print(num)
print(twice[:800])


bs = BeautifulSoup('<p><a>惟有痴情难学佛</a>独无媚骨不如人</p>','html.parser')

tag = bs.find('p')

print(tag.text)