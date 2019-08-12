import requests
from bs4 import BeautifulSoup
# 引用requests库
commentid = ''
header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    'Sec-Fetch-Mode': 'cors',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }
url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
for i in range(200):
    params ={
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'GB2312',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0',
        'cid': '205360772',
        'reqtype': '2',
        'biztype': '1',
        'topid': '102065750',
        'cmd': '8',
        'needmusiccrit': '0',
        'pagenum': str(i),
        'pagesize': '25',
        'lasthotcommentid': commentid,
        'domain': 'qq.com',
        'ct': '24',
        'cv': '10101010',
    }
    
    res_comment = requests.get(url,params=params,headers=header)
    res_json = res_comment.json()
    list_comment = res_json['comment']['commentlist']
    for comment in list_comment:
        print(comment['rootcommentcontent'])
    commentid = list_comment[24]['commentid']
    print('第'+str(i)+'页读取完毕')


    
    
    # # 调用get方法，下载这个字典
    # json_music = res_music.json()
    # # 使用json()方法，将response对象，转为列表/字典

    # list_music = json_music['data']['song']['list']

    # # 一层一层地取字典，获取歌单列表
    # for music in list_music:
    # # list_music是一个列表，music是它里面的元素
    #     print(music['title'])
    #     # 以name为键，查找歌曲名
    #     print(music['album']['name'])
    #     # 专辑名
    #     print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n')
        
    #     # 播放链接
    #     url = 'https://y.qq.com/n/yqq/song/'+music['mid']+'.html'
    #     res = requests.get(url)
    #     html = BeautifulSoup(res.text,'html.parser')
    #     music_word = html.find_all('div',class_="lyric__c   ont_box")
    #     print(music_word)


    