import  requests
from bs4 import  BeautifulSoup
import  re

headers={
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
     "referer":"https://image.baidu.com"
    }

url ="https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C3%C0%C5%AE&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111"

re = requests.get(url,headers=headers)
# re = requests.get(url)

doms = BeautifulSoup(re.text,"html.parser")
# print(doms.prettify())
# for x in doms.find_all('div',attrs={"class":"imgpage"}):
# for x in doms.find_all(attrs={'id':'wrapper'}):
# # for x in doms.find_all('img'):
#     print(x)
#     print(x.get("class"))
#     # print(x.get('src'))

import  urllib
rep=urllib.request.Request(url,headers=headers)
rep=urllib.request.urlopen(rep)
    #读取网页数据
html=rep.read().decode("utf-8")
print(html)
