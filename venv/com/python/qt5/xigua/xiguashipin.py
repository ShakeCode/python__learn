import base64
import json
import logging
import os
import re
import time
from moviepy import *
from moviepy.editor import *
import requests
# https://blog.csdn.net/qq_33516409/article/details/119855258
from selenium import webdriver

logFile = 'xigua.log'
formatStr11 = '%(asctime)s - %(name)s - process_id: %(process)s - thread_id: %(thread)d - %(filename)s - %(levelname)s - %(lineno)d: %(message)s'
# 输出文件
logging.basicConfig(filename=logFile, format=formatStr11,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)

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
    "Referer": "https://www.ixigua.com"
    # "Cookie":"__ac_nonce=06122217b0057aec2e7ce; __ac_signature=_02B4Z6wo00f01HiyszAAAIDBG7hzW.3penR4kreAAH8W6f; __ac_referer=__ac_blank; ttcid=5d55ea80f73040bc8f7c1211ed58458a48; MONITOR_WEB_ID=50984067-b35f-484a-a7dd-bed58d13bc71; ttwid=1%7Cb3BvZjY5ybfG0cQfXCc00jjr8rQnM8aSZL8WE6BdLu8%7C1629626748%7C14ca7b64258bf402324c3cdee546221029a261bb6a3a3d34fe353682f41e49a2"
}


def getVideoUrl(url: str, needAudio: bool):
    session = requests.session()
    # Max retries exceeded with url错误
    session.keep_alive = False
    requests.adapters.DEFAULT_RETRIES = 10

    # 抑制证书警告
    requests.packages.urllib3.disable_warnings()
    # 需要先访问一次视频网站获取cookies才行
    session.get(url, headers=headers, verify=False)
    response = session.get(url + "?wid_try=1", headers=headers, verify=False)
    logger.info('first return json: %s ', response)
    logger.info('response.text: %s ', json.dumps(response.text))
    # response.encoding = "UTF-8"
    # 只取720P
    it = re.search(r'definition":"720p"[\s|\S]*?main_url":"(?P<main_url>.*?)"', response.text, re.S)
    logger.info('目标地址, mainUrl data: %s', it)
    # .decode('ascii') 去除字符串b
    no_watermark_downloadUrl = base64.b64decode(it.group("main_url")).decode('ascii')
    logger.info('无水印播放地址 analysis b64decode main_url: %s', no_watermark_downloadUrl)
    # 转码
    logger.info('响应编码是, response.apparent_encoding: %s', response.apparent_encoding)
    response.encoding = response.apparent_encoding
    logger.info('转码后 响应数据: %s', json.dumps(response.text))
    title = re.findall('<title data-react-helmet="true">(.*?)</title>', response.text)[0].replace(' - 西瓜视频', '')
    logger.info('[ 视频标题, title : %s ]', title)
    watermark_downloadUrl = re.findall('"embedUrl":"(.*?)"', response.text)[0]
    logger.info('带水印播放地址: %s', watermark_downloadUrl)
    no_watermark_downloadUrl = str(no_watermark_downloadUrl).replace(r".\xd3M\x85", "?")
    logger.info('无水印播放地址: %s , type: %s ', no_watermark_downloadUrl, type(no_watermark_downloadUrl))

    #######################################################################
    if not needAudio:
        return {'no_watermark_downloadUrl': no_watermark_downloadUrl, 'title': title}

    pattern = re.compile('(?<=window._SSR_HYDRATED_DATA=).*?(?=</script>)')
    jsonResult = pattern.findall(response.text)[0]
    jsonResult = jsonResult.replace(':undefined', ':"undefined"')
    jsonData = json.loads(jsonResult)
    logger.debug('json result: %s', jsonResult)
    infor = jsonData['anyVideo']['gidInformation']['packerData']['video']
    dash = infor['videoResource']['dash']
    if 'dynamic_video' in dash.keys():
        audioUrl = dash['dynamic_video']['dynamic_audio_list'][0]['main_url']
        videoUrl = dash['dynamic_video']['dynamic_video_list'][0]['main_url']
    else:
        print('未获取到源地址')
    audio_url = base64.b64decode(audioUrl).decode("utf-8")
    video_url = base64.b64decode(videoUrl).decode("utf-8")

    logger.info("音频地址: %s", audio_url)
    logger.info("视频频地址: %s", video_url)
    #######################################################################

    return {'no_watermark_downloadUrl': no_watermark_downloadUrl, 'title': title,
            'watermark_downloadUrl': watermark_downloadUrl, 'audio_url': audio_url}


def doDownLoad(url: str, local_save_path: str, fileName: str, fileTypeSuffix: str) -> None:
    logger.info('doDownLoad param url: %s, save_path: %s, fileName:　%s', url, local_save_path, fileName)
    """
    下载视频到本地目录
    :param url: 下载地址
    :param local_save_path: 本地文件保存路径 命名方式: file +filename 注意需要指定文件名，否则报错
    :return:
    """
    try:
        start = time.time()  # 下载开始时间
        # requests发送浏览器发送get请求,得到数据
        response = requests.get(url=url, headers=headers, stream=True)
        print(response)  # 输出r访问状态
        # 获取数据的二进制长度
        reponse_body_lenth = int(response.headers.get("Content-Length"))

        # 如果不存在则创建视频文件夹存放视频
        if not os.path.exists(local_save_path):
            os.mkdir(local_save_path)

            # 打印数据的长度
            # path_1为完整文件保存路径
        path_1 = (local_save_path + fileName + fileTypeSuffix)
        print("视频:%s  数据长度为:%s   保存文件：%s" % (url, reponse_body_lenth, path_1))

        if os.path.exists(path_1):
            print("视频已存在!")
            return
        size = 0  # 初始化已下载大小
        chunk_size = 1024000  # 每次下载的数据大小
        content_size = int(response.headers['content-length'])  # 下载文件总大小
        print('Start download,[File size]:{size:.2f} MB'.format(size=content_size / chunk_size / 1024))
        # 保存抖音视频mp4格式，二进制读取
        # with open(path_1, "wb") as xh:
        with open((f"{local_save_path}\{fileName}{fileTypeSuffix}"), "wb") as xh:
            # 先定义初始进度为0
            write_all = 0
            for data in response.iter_content(chunk_size=chunk_size):
                write_all += xh.write(data)
                size += len(data)
                # 打印下载进度
                # print("下载进度：%0.2d%%" % (100 * write_all / reponse_body_lenth))
                print('[下载进度]:%s  %.2f%%' % ('▇' * int(size * 50 / content_size), float(size / content_size * 100)),
                      end='\n')
            # print(f"file:{url} download success!")
        end = time.time()  # 下载结束时间
        print('Download completed!, waste times: %.2f秒' % (end - start))  # 输出下载用时时间
        print(f'视频[ {fileName} ]已经保存完毕')
    except Exception as e:
        print(f"downLoad file error,please check whether the file path is correct!\nerror massage：{e} ")
        raise e
        print("download success!")


def get_video_url(html_url):
    """传入播放地址，获取视频下载地址"""
    driver = webdriver.Edge()
    time.sleep(2)

    driver.get(html_url)
    driver.set_window_size(1936, 1056)
    driver.implicitly_wait(10)
    video_url = driver.find_element_by_css_selector('#player_default video').get_attribute('src')
    driver.close()
    return video_url


def mergeAudioVideo(path, title):
    '''合并音频和视频
    https://blog.csdn.net/weixin_42750611/article/details/125115867?spm=1001.2101.3001.6650.5&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-5-125115867-blog-110625602.pc_relevant_3mothn_strategy_recovery&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-5-125115867-blog-110625602.pc_relevant_3mothn_strategy_recovery&utm_relevant_index=7
    '''
    video_path = path + title + '.mp4'
    audio_path = path + title + '.mp3'
    # 提取音轨
    audio = AudioFileClip(audio_path)
    # 读入视频
    video = VideoFileClip(video_path)
    # 将音轨合并到视频中
    video = video.set_audio(audio)
    # 输出
    video.write_videofile(f"{path}+{title}(含音频).mp4")


# url = "https://www.ixigua.com/6704446868685849092"
# url = "https://www.ixigua.com/6986561438525424165"
url = "https://www.ixigua.com/7048552544691290631"

# 是否下载音频
needAudio = True

# 是否需要合并视频
needMerge = True
response = getVideoUrl(url, needAudio)

# 获取真实视频地址
# print('播放地址: %s ' % get_video_url(response['watermark_downloadUrl']))

# 下载视频
doDownLoad(response['no_watermark_downloadUrl'], 'D:\\', fileName=response['title'], fileTypeSuffix='.mp4')

if needAudio:
    # 下载音频
    doDownLoad(response['audio_url'], 'D:\\', fileName=response['title'], fileTypeSuffix='.mp3')
if needMerge:
    # 合并音频视频
    mergeAudioVideo('D:\\', response['title'])
