import json
import logging
import re

import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()

formatStr11 = '%(asctime)s - %(name)s - process_id: %(process)s - thread_id: %(thread)d - %(filename)s - %(levelname)s - %(lineno)d: %(message)s'
# 输出文件
# logging.basicConfig(format=formatStr11,
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     level=logging.DEBUG)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter(formatStr11))
logger.addHandler(streamHandler)

headers = {
    "Connection": "keep-alive",
    "Cache-Control": "no-cache",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Dest": "document",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "sec-ch-ua": "Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
    "Referer": "",
    "sec-ch-ua-mobile": "?0"
    # "Cookie":"__ac_nonce=06122217b0057aec2e7ce; __ac_signature=_02B4Z6wo00f01HiyszAAAIDBG7hzW.3penR4kreAAH8W6f; __ac_referer=__ac_blank; ttcid=5d55ea80f73040bc8f7c1211ed58458a48; MONITOR_WEB_ID=50984067-b35f-484a-a7dd-bed58d13bc71; ttwid=1%7Cb3BvZjY5ybfG0cQfXCc00jjr8rQnM8aSZL8WE6BdLu8%7C1629626748%7C14ca7b64258bf402324c3cdee546221029a261bb6a3a3d34fe353682f41e49a2"
}


def getAllHtmlUrl(url):
    global pattern, script
    source_code = requests.get(url, headers=headers)
    # just get the code, no headers or anything
    plain_text = source_code.text
    # BeautifulSoup objects can be sorted through easy
    # soup = BeautifulSoup(plain_text, features="lxml")
    soup = BeautifulSoup(plain_text, "html.parser")
    tarList = soup.find_all('div', class_='stui-pannel_bd col-pd clearfix')
    # w云 div
    playDiv = tarList[1]
    logger.info('div 长度: %s', tarList.__len__())
    logger.info('div 数据: %s', playDiv)
    # <class 'bs4.element.ResultSet'>
    logger.info('播放列表div 类型: %s', type(playDiv))
    playDivUl = playDiv.find('ul', class_='stui-content__playlist column8 clearfix')
    logger.info('div ul 数据: %s', playDivUl)
    # playDivUlli = playDiv.findAll('li', class_='active')
    # logger.info('div ul li数据: %s',playDivUlli)
    playUrl = []
    baseUrl = 'https://www.zbkk.net'
    for li in playDivUl:
        playUrl.append(baseUrl + li.find('a')['href'])
    logger.info("播放html列表: %s", playUrl)
    return playUrl
    # playVeDiv = soup.find_all('div', class_='stui-player__video embed-responsive embed-responsive-16by9 clearfix')
    # logger.info('播放div script 内容: %s', playVeDiv)
    # # 获取script的变量数据
    # pattern = re.compile(r"var player_aaaa=(.*?)$", re.MULTILINE | re.DOTALL)
    # script = soup.find('script', text=pattern)
    # script11 = soup.findAll('script', attrs={'type': 'text/javascript'})
    # data_str = pattern.search(script.text).group(1)
    # data_json = json.loads(data_str, strict=False)
    # logger.info("var 变量值: %s", data_json)
    # logger.info("index.mu38 地址: %s", data_json['url'])


def getMu38Url(url):
    global pattern, script
    source_code = requests.get(url, headers=headers)
    # just get the code, no headers or anything
    plain_text = source_code.text
    # BeautifulSoup objects can be sorted through easy
    # soup = BeautifulSoup(plain_text, features="lxml")
    soup = BeautifulSoup(plain_text, "html.parser")
    tarList = soup.find_all('div', class_='stui-pannel_bd col-pd clearfix')
    # w云 div
    playDiv = tarList[1]
    logger.info('div 长度: %s', tarList.__len__())
    logger.info('div 数据: %s', playDiv)
    # <class 'bs4.element.ResultSet'>
    logger.info('播放列表div 类型: %s', type(playDiv))
    playDivUl = playDiv.find('ul', class_='stui-content__playlist column8 clearfix')
    logger.info('div ul 数据: %s', playDivUl)
    # playDivUlli = playDiv.findAll('li', class_='active')
    # logger.info('div ul li数据: %s',playDivUlli)
    # playUrl = []
    # baseUrl = 'https://www.zbkk.net'
    # for li in playDivUl:
    #     playUrl.append(baseUrl + li.find('a')['href'])
    # logger.info("播放html列表: %s", playUrl)
    playVeDiv = soup.find_all('div', class_='stui-player__video embed-responsive embed-responsive-16by9 clearfix')
    logger.info('播放div script 内容: %s', playVeDiv)
    # 获取script的变量数据
    pattern = re.compile(r"var player_aaaa=(.*?)$", re.MULTILINE | re.DOTALL)
    script = soup.find('script', text=pattern)
    script11 = soup.findAll('script', attrs={'type': 'text/javascript'})
    data_str = pattern.search(script.text).group(1)
    data_json = json.loads(data_str, strict=False)
    logger.info("var 变量值: %s", data_json)
    logger.info("index.mu38 地址: %s", data_json['url'])
    return data_json['url']


def withWriteFile(path, paramList):
    '''with 操作文件'''
    with open(path, 'w+', encoding='utf-8') as f:
        try:
            for line in paramList:
                f.write(line)
                f.write('\n')
        except Exception as e:
            print('写入文件异常...', e)


url = "https://www.zbkk.net/zbkplay/440-1-1.html"

htmlList = getAllHtmlUrl(url)

logger.info("获取所有播放地址HTML: %s", htmlList)
logger.info("获取所有播放地址HTML 大小: %s", len(htmlList))

htmlPageFile = '播放html集合.txt'
# 记录获取所有播放地址HTML
withWriteFile(htmlPageFile, htmlList)

allMu38Url = []
for url in htmlList:
    mu38Result = getMu38Url(url)
    allMu38Url.append(mu38Result)

logger.info("获取所有allMu38Url: %s", allMu38Url)
logger.info("allMu38Url 大小: %s", len(allMu38Url))

allMu38UrlPageFilePath = '视频mu38-url集合.txt'
# 记录获取所有播放地址HTML
withWriteFile(allMu38UrlPageFilePath, allMu38Url)

allHlsMu38UrlPageFilePath = '视频hls-mu38-url集合.txt'
# 记录获取所有最终分片的播放mu38地址
allHlsMu38Url = []
for ss in allMu38Url:
    allHlsMu38Url.append(ss[0:40] + "hls/" + ss[-10:])
withWriteFile(allHlsMu38UrlPageFilePath, allHlsMu38Url)

ss = 'https://v5.cdtlas.com/20220625/WIMip8Jc/index.m3u8'
# index.m3u8 部分
# print(ss[-10:])
# https://v5.cdtlas.com/20220625/ORG5ObUm部分
# print(ss[0:40])

# 获取/index.m3u8 请求得到/hls/index.m3u8 的地址, 中间相差/hls

# 获取/hls/index.m3u8

'''
https://v5.cdtlas.com/20220625/ORG5ObUm/index.m3u8

https://v5.cdtlas.com/20220625/ORG5ObUm/hls/index.m3u8

'''

'''
/zbkplay/440-1-1.html 
到
/zbkplay/440-1-95.html
'''
