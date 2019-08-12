import requests
res=requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
data = res.content
f= open('music.mp3','wb')
f.write(data)
f.close()
