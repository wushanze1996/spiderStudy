import requests #调用requests库
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
#获取网页源代码，得到的res是Response对象
html=res.text
#把res的内容以字符串的形式返回
print('响应状态码:',res.status_code) #检查请求是否正确响应
print(html) #打印网页源代码