import requests
from bs4 import BeautifulSoup
url = 'https://www.ygdy8.com/'
res = requests.get(url)
res.encoding='GBK'
soup = BeautifulSoup(res.text,'html.parser')
movie_list = soup.find_all('div',class_="co_content4")
list_movies = []
for movies in movie_list:
    movie_a = movies.find_all('a')
    for movie in movie_a:
        movie_name = movie.text
        print(movie_name)
        href = movie['href']
        movie_href = 'https://www.ygdy8.com/'+href
        print(movie_href)
        resq = requests.get(movie_href)
        resq.encoding='GBK'
        soup2 = BeautifulSoup(resq.text,'html.parser')
        links = soup2.find_all('tbody')
        for l in links:
             link = l.find('a')
             link_href = link['href']
             print(link_href)
             strs ='电影名：'+movie_name+'下载地址：'+link_href
             with open('ygdy.txt','a',encoding='utf-8') as f:
                 f.write(strs)
print('完成采集')
    
