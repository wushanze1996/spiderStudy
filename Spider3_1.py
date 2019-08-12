import requests
from bs4 import BeautifulSoup
num = 1
for i in range(10):
    url = f"https://movie.douban.com/top250?start={i*25}&filter="
    print(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    list_movie = soup.find_all('div',class_="item")

    for movies in list_movie:
        
       
        movie = movies.find('a')
        movie_rating_num = movies.find('span',class_="rating_num").text
        movie_name = movies.find('span',class_="title").text
        movie_href=movie['href']
        strs = '\n序号：'+str(num) + '\n电影名：'+movie_name+'\n电影链接：'+movie_href+'\n电影评分'+movie_rating_num
        with open('movies_list.txt','a',encoding='utf-8') as f:
            f.write(strs)
            f.close()
        print(strs)
        num=num+1
        
        
