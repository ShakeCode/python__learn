import concurrent.futures
# from Crypto.Cipher import AES
import glob
import logging
import os
import re
import time
from concurrent.futures import as_completed

import m3u8
import requests
import urllib3
from cryptography.hazmat.primitives.ciphers.algorithms import AES

logFile = '下载三国视频日志.log'
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

# 禁止证书警告(InsecureRequestWarning: Unverified HTTPS request is being made to host 'hey08.cjkypo.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings)
urllib3.disable_warnings()
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


# 正则表达判断是否为网站地址
def reurl(url):
    pattern = re.compile(r'^((https|http|ftp|rtsp|mms)?:\/\/)[^\s]+')
    m = pattern.search(url)
    if m is None:
        return False
    else:
        return True


# 获取密钥
def getKey(keystr, url):
    keyinfo = str(keystr)
    method_pos = keyinfo.find('METHOD')
    comma_pos = keyinfo.find(",")
    method = keyinfo[method_pos:comma_pos].split('=')[1]
    uri_pos = keyinfo.find("URI")
    quotation_mark_pos = keyinfo.rfind('"')
    key_url = keyinfo[uri_pos:quotation_mark_pos].split('"')[1]
    if reurl(key_url) == False:
        key_url = url.rsplit("/", 1)[0] + "/" + key_url
    res = requests.get(key_url, headers=headers)
    key = res.content
    logger.info(method)
    logger.info(key.decode('utf-8'))
    return method, key


# 下载文件
# down_url:ts文件地址
# url:*.m3u8文件地址
# decrypt:是否加密
# down_path:下载地址
# key:密钥
def download(fileIndex, down_url, url, decrypt, down_path, key):
    if reurl(down_url) == False:
        filename = down_url
        down_url = url.rsplit("/", 1)[0] + "/" + down_url
    else:
        filename = down_url.rsplit("/", 1)[1]
    try:
        res = requests.get(down_url, stream=True, verify=False, headers=headers)
    except Exception as e:
        logger.info(e)
        return
    down_ts_path = down_path + "/{0}.ts".format(fileIndex)
    logger.info(
        "response code:{0}, download ts, fileIndex{1} fileName:{2},down_ts_path:{3}".format(res, fileIndex, filename,
                                                                                            down_ts_path))
    if decrypt:
        cryptor = AES.new(key, AES.MODE_CBC, key)
    with open(down_ts_path, "wb+") as file:
        for chunk in res.iter_content(chunk_size=1024 * 100):
            if chunk:
                if decrypt:
                    file.write(cryptor.decrypt(chunk))
                else:
                    file.write(chunk)

    logger.info("write success,download down_ts_path:{0}".format(down_ts_path))


# 合并ts文件
# dest_file:合成文件名
# source_path:ts文件目录
# ts_list:文件列表
# delete:合成结束是否删除ts文件
def merge_to_mp4(dest_file, source_path, ts_list, delete=False):
    logger.info("start merge_to_mp4, dest file: %s, source_path:%s, ts size:%s", dest_file, source_path, len(ts_list))
    # files = glob.glob(source_path + '/*.ts')
    files = os.listdir(source_path)
    # 对‘.’进行切片，并取列表的第一个值（左边的文件名）转化整数型
    files.sort(key=lambda x:int(x.split('.')[0]))
    logger.info("all ts file size: %s", len(files))
    '''
    if len(files) != len(ts_list):
        logger.info("文件不完整！")
        return
    '''
    with open(dest_file, 'wb') as fw:
        for file in files:
            with open(source_path + '/' + file, 'rb') as fr:
                fw.write(fr.read())
            if delete:
                os.remove(file)


def dir_file_delete(dir):
    files = os.listdir(dir)
    os.chdir(dir)  # 进入指定目录
    # 遍历删除指定目录下的文件
    for file in files:
        os.remove(file)
        logger.info(file, "删除成功")
    # os.chdir("..")
    # logger.info(os.path)
    # os.remove(dir)
    # logger.info(dir,"删除成功")


def main():
    # url = "https://m3u8.zhisongip.com:38741/video/65b4b1b505ce6fcd196cacb0fab2a432.m3u8"
    url = "https://v5.cdtlas.com/20220625/WIMip8Jc/hls/index.m3u8"
    # 使用m3u8库获取文件信息
    video = m3u8.load(url)
    # 设置下载路径
    down_path = "tmp"
    # 设置是否加密标志
    decrypt = False
    # ts列表
    ts_list = []
    decryptKery = ''
    # 判断是否加密
    if video.keys[0] is not None:
        method, key = getKey(video.keys[0], url)
        decryptKery = key
        decrypt = True
        # 删除旧文件

    logger.info("目录为: %s" % os.listdir(os.getcwd()))
    # os.remove('tmp')

    # 判断是否需要创建文件夹
    if not os.path.exists(down_path):
        os.mkdir(down_path)
    else:
        logger.info("目录已经存在")
        # 去除目录只读属性
        # os.system(f"attrib -r {down_path}")
        # dir_file_delete(down_path)

    # 把ts文件名添加到列表中
    for filename in video.segments:
        if reurl(filename.uri):
            ts_list.append(filename.uri.rsplit("/", 1)[1])
        else:
            ts_list.append(filename.uri)
    logger.info("video.segments, ts片段大小:{0}".format(len(video.segments)))
    logger.info("ts_list大小:{0}".format(len(ts_list)))
    # 开启线程池
    with concurrent.futures.ThreadPoolExecutor() as executor:
        obj_list = []
        begin = time.time()  # 记录线程开始时间
        for i in range(len(video.segments)):
            obj = executor.submit(download, i + 1, video.segments[i].uri, url, decrypt, down_path, decryptKery)
            # 异常回调异常日志打印
            obj.add_done_callback(thread_pool_callback)
            obj_list.append(obj)
        # 查看线程池是否结束
        for future in as_completed(obj_list):
            data = future.result()
            logger.info(data)
        # 合并所有ts文件为mp4格式
        merge_to_mp4('result.mp4', down_path, ts_list)  # 合并ts文件
        times = time.time() - begin  # 记录线程完成时间
        logger.info("合并完成, 耗时: %s s", times)


def thread_pool_callback(worker):
    logger.debug("called thread pool executor callback function")
    worker_exception = worker.exception()
    if worker_exception:
        logger.exception("Worker return exception: {}".format(worker_exception))


def testMergeTs():
    global begin
    fileName = '新三国第{0}集.mp4'.format(1)
    begin = time.time()
    merge_to_mp4('H:/python_ts/' + fileName, 'tmp', [])  # 合并ts文件
    times = time.time() - begin  # 记录线程完成时间
    logger.info("合并完成, 耗时: %s s", times)


if __name__ == "__main__":
    main()
    # testMergeTs()
