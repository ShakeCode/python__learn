import concurrent.futures
# from Crypto.Cipher import AES
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
formatStr11 = '%(asctime)s - %(name)s - process_id: %(process)s - thread_name: %(threadName)s - thread_id: %(thread)d - %(filename)s - %(levelname)s - %(lineno)d: %(message)s'
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
    res = requests.get(key_url, headers=headers, timeout=360)
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
        res = requests.get(down_url, stream=True, verify=False, headers=headers, timeout=360)
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


def downloadVedio(video, fileIndex, mu38Url):
    beginA = time.time()
    # 设置下载路径
    # 设置是否加密标志
    decrypt = False
    decryptKery = ''
    # 判断是否加密
    if video.keys[0] is not None:
        method, key = getKey(video.keys[0], mu38Url)
        decryptKery = key
        decrypt = True
        # 删除旧文件

    logger.debug("目录为: %s" % os.listdir(os.getcwd()))
    # os.remove('tmp')

    down_path = "H:/python_ts/"
    # 判断是否需要创建文件夹
    savePath = down_path + "第{0}集ts".format((str(fileIndex)))
    logger.info("第%s集ts存放目录:%s", fileIndex, savePath)
    # 创建多级目录
    mkdir_multi(savePath)
    # if not os.path.exists(savePath):
    #     # os.mkdir(down_path)
    #     # 创建多级目录
    #     os.makedirs(down_path)
    # else:
    #     logger.info("目录已经存在")
    #     # 去除目录只读属性
    #     # os.system(f"attrib -r {down_path}")
    #     # dir_file_delete(down_path)

    # 把ts文件名添加到列表中
    # ts列表
    ts_list = []
    for filename in video.segments:
        if reurl(filename.uri):
            ts_list.append(filename.uri.rsplit("/", 1)[1])
        else:
            ts_list.append(filename.uri)
    logger.info("video.segments, ts片段大小:{0}".format(len(video.segments)))
    logger.info("ts_list大小:{0}".format(len(ts_list)))
    # 分片下載
    for i in range(len(video.segments)):
        down_url = video.segments[i].uri
        if reurl(down_url) == False:
            filename = down_url
            down_url = mu38Url.rsplit("/", 1)[0] + "/" + down_url
        else:
            filename = down_url.rsplit("/", 1)[1]
        try:
            res = requests.get(down_url, stream=True, verify=False, headers=headers, timeout=360)
        except Exception as e:
            logger.info(e)
            return
        # ts下载地址
        down_ts_path = savePath + "/{0}.ts".format(i + 1)
        logger.info(
            "response code:{0}, download ts, fileIndex{1} fileName:{2},down_ts_path:{3}".format(res, fileIndex,
                                                                                                filename,
                                                                                                down_ts_path))
        if decrypt:
            cryptor = AES.new(key, AES.MODE_CBC, key)

        exists = os.path.exists(down_ts_path)
        if exists:
            fileSize = os.path.getsize(down_ts_path)
            logger.debug("size: %s", fileSize)

        if exists and len(res.content) == fileSize:
            continue

        ifContinue = False

        with open(down_ts_path, "wb+") as file:
            aa = 0;
            for chunk in res.iter_content(chunk_size=1024 * 1000):
                if exists and fileSize == len(chunk):
                    logger.info("%s 已存在,且文件流大小相等, 跳过下载...", down_ts_path)
                    ifContinue = True
                    break
                if chunk:
                    if decrypt:
                        file.write(cryptor.decrypt(chunk))
                    else:
                        aa += len(chunk)
                        file.write(chunk)
            logger.debug("chunk size:%s", len(chunk))

        if ifContinue:
            continue

        logger.info("write success,download down_ts_path:{0}".format(down_ts_path))
    fileName = '新三国第{0}集.mp4'.format(fileIndex)
    # 记录下载完成时间
    times = time.time() - beginA
    logger.info("%s下载完成, 耗时: %s s", fileName, times)

    # 合并所有ts文件为mp4格式
    begin = time.time()
    merge_to_mp4('H:/python_ts/' + fileName, savePath, ts_list)  # 合并ts文件
    times = time.time() - begin
    # 记录合并完成时间
    logger.info("%s合并完成, 耗时: %s s", fileName, times)


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
    files.sort(key=lambda x: int(x.split('.')[0]))
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


def withReadFile(path, rowIndexList: list):
    '''with 操作文件'''
    dataPathMap = {}
    count = -1
    for count, line in enumerate(open(path, 'rU')):
        count += 1
    print(count)
    with open(path, 'r+', encoding='utf-8') as f:
        try:
            for index, rowDate in enumerate(f):
                line = rowDate
                if len(rowIndexList) == 0:
                    # 下载全部
                    # 去除末尾\n
                    dataPathMap[index + 1] = line.rstrip('\n')
                else:
                    if not rowIndexList.__contains__(index + 1):
                        continue
                    else:
                        # 下载全部
                        # 去除末尾\n
                        dataPathMap[index + 1] = line.rstrip('\n')
        except Exception as e:
            print('读取文件异常...', e)
            raise e
    return dataPathMap


def mkdir_multi(path):
    # 判断路径是否存在
    isExists = os.path.exists(path)

    if not isExists:
        # 如果不存在，则创建目录（多层）
        os.makedirs(path)
        print('目录创建成功！')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print('目录已存在！')
        return False


def downloadAllSeries(filePath, targetList):
    # url = "https://m3u8.zhisongip.com:38741/video/65b4b1b505ce6fcd196cacb0fab2a432.m3u8"
    # [1,2]下载第一,二集, []下载全部
    # mu38UrlList = withReadFile(filePath, [1,2,3,4])
    mu38UrlMap = withReadFile(filePath, targetList)
    logger.info("下载剧集数量: %s", len(mu38UrlMap))
    # url = "https://v5.cdtlas.com/20220625/WIMip8Jc/hls/index.m3u8"
    # 开启线程池
    obj_list = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50, thread_name_prefix='async') as executor:
        for videIndex, mu38Url in mu38UrlMap.items():
            logger.info("开始下载第%s集视频, mu38-url:%s", videIndex, mu38Url)
            # 使用m3u8库获取文件信息
            video = m3u8.load(mu38Url)
            obj = executor.submit(downloadVedio, video, videIndex, mu38Url)
            # 异常回调异常日志打印
            obj.add_done_callback(thread_pool_callback)
            obj_list.append(obj)

    try:
        # 查看线程池是否结束
        # as_completed添加超时时间，如果不添加，则此线程池一直存在
        for future in as_completed(obj_list, 2):
            data = future.result()
            logger.info("异步下载结果: %s", data)
    except TimeoutError as e:
        # 清除相关资源，参数 默认为True,需要 所有线程都返回数据才清空资源;参数为 False,则直接清空资源,继续执行后续程序
        executor.shutdown(False)
        print('shut down!')


def thread_pool_callback(worker):
    logger.debug("called thread pool executor callback function")
    worker_exception = worker.exception()
    if worker_exception:
        logger.exception("Worker return exception: {}".format(worker_exception))


def downloadOneSeriesByMutilThread(filePath, listData):
    # url = "https://m3u8.zhisongip.com:38741/video/65b4b1b505ce6fcd196cacb0fab2a432.m3u8"
    # [1,2]下载第一,二集, []下载全部
    # mu38UrlList = withReadFile(filePath, [1,2,3,4])
    mu38UrlMap = withReadFile(filePath, listData)
    logger.info("下载剧集数量: %s", len(mu38UrlMap))
    # url = "https://v5.cdtlas.com/20220625/WIMip8Jc/hls/index.m3u8"
    # 开启线程池
    for videIndex, mu38Url in mu38UrlMap.items():
        logger.info("开始下载第%s集视频, mu38-mu38Url:%s", videIndex, mu38Url)
        downloadOneVideo(mu38Url, videIndex)


def downloadOneVideo(mu38Url, fileIndex):
    beginA = time.time()
    # 使用m3u8库获取文件信息
    video = m3u8.load(mu38Url)

    # 设置下载路径
    # 设置是否加密标志
    decrypt = False
    decryptKey = ''
    # 判断是否加密
    if video.keys[0] is not None:
        method, key = getKey(video.keys[0], mu38Url)
        decryptKey = key
        decrypt = True
        # 删除旧文件

    logger.debug("目录为: %s" % os.listdir(os.getcwd()))
    # os.remove('tmp')

    down_path = "H:/python_ts/"
    # 判断是否需要创建文件夹
    savePath = down_path + "第{0}集ts".format((str(fileIndex)))
    logger.info("第%s集ts存放目录:%s", fileIndex, savePath)
    # 创建多级目录
    mkdir_multi(savePath)
    # if not os.path.exists(savePath):
    #     # os.mkdir(down_path)
    #     # 创建多级目录
    #     os.makedirs(down_path)
    # else:
    #     logger.info("目录已经存在")
    #     # 去除目录只读属性
    #     # os.system(f"attrib -r {down_path}")
    #     # dir_file_delete(down_path)

    # 把ts文件名添加到列表中
    # ts列表
    ts_list = []
    for filename in video.segments:
        if reurl(filename.uri):
            ts_list.append(filename.uri.rsplit("/", 1)[1])
        else:
            ts_list.append(filename.uri)
    logger.info("video.segments, ts片段大小:{0}".format(len(video.segments)))
    logger.info("ts_list大小:{0}".format(len(ts_list)))

    obj_list = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50, thread_name_prefix='async') as executor:
        # 分片下載
        for index in range(len(video.segments)):
            segmentUrl = video.segments[index].uri
            obj = executor.submit(downloadOneSeriesVedio, decrypt, decryptKey, savePath, index + 1, segmentUrl, mu38Url)
        # 异常回调异常日志打印
        obj.add_done_callback(thread_pool_callback)
        obj_list.append(obj)

    try:
        # 查看线程池是否结束
        # as_completed添加超时时间，如果不添加，则此线程池一直存在
        for future in as_completed(obj_list, 2):
            data = future.result()
            logger.info("异步下载结果: %s", data)
    except TimeoutError as e:
        # 清除相关资源，参数 默认为True,需要 所有线程都返回数据才清空资源;参数为 False,则直接清空资源,继续执行后续程序
        executor.shutdown(False)
        print('shut down!')

    fileName = '新三国第{0}集.mp4'.format(fileIndex)
    # 记录下载完成时间
    times = time.time() - beginA
    logger.info("%s下载完成, 耗时: %s s", fileName, times)

    # 合并所有ts文件为mp4格式
    begin = time.time()
    merge_to_mp4('H:/python_ts/' + fileName, savePath, ts_list)  # 合并ts文件
    times = time.time() - begin
    # 记录合并完成时间
    logger.info("%s合并完成, 耗时: %s s", fileName, times)


def downloadOneSeriesVedio(decrypt, decryptKey, savePath, segmentIndex, segmentUrl, mu38Url):
    # 分片下載
    down_url = segmentUrl
    if reurl(down_url) == False:
        filename = down_url
        down_url = mu38Url.rsplit("/", 1)[0] + "/" + down_url
    else:
        filename = down_url.rsplit("/", 1)[1]
    try:
        res = requests.get(down_url, stream=True, verify=False, headers=headers, timeout=360)
    except Exception as e:
        logger.info(e)
        return
    # ts下载地址
    down_ts_path = savePath + "/{0}.ts".format(segmentIndex)
    logger.info(
        "response code:{0}, download ts, fileIndex: {1} fileName:{2},down_ts_path:{3}".format(res, segmentIndex,
                                                                                              filename,
                                                                                              down_ts_path))
    if decrypt:
        cryptor = AES.new(decryptKey, AES.MODE_CBC, decryptKey)

    exists = os.path.exists(down_ts_path)
    fileSize = 0
    if exists:
        fileSize = os.path.getsize(down_ts_path)
        logger.debug("size: %s", fileSize)

    if exists and len(res.content) == fileSize:
        return

    ifContinue = False
    with open(down_ts_path, "wb+") as file:
        aa = 0
        for chunk in res.iter_content(chunk_size=1024 * 1000):
            if exists and fileSize == len(chunk):
                logger.info("%s 已存在,且文件流大小相等, 跳过下载...", down_ts_path)
                ifContinue = True
                break
            if chunk:
                if decrypt:
                    file.write(cryptor.decrypt(chunk))
                else:
                    aa += len(chunk)
                    file.write(chunk)
        logger.debug("chunk size:%s", len(chunk))

    if ifContinue:
        return
    logger.info("write ts data success,download down_ts_path:{0}".format(down_ts_path))
    return "as_completed, write ts data success,download down_ts_path:{0}".format(down_ts_path)


# def testMergeTs():
#     global begin
#     fileName = '新三国第{0}集.mp4'.format(1)
#     begin = time.time()
#     merge_to_mp4('H:/python_ts/' + fileName, 'tmp', [])  # 合并ts文件
#     times = time.time() - begin  # 记录线程完成时间
#     logger.info("合并完成, 耗时: %s s", times)

if __name__ == "__main__":
    filePath = '视频hls-mu38-url集合.txt'
    # downloadAllSeries(filePath, [1])
    downloadOneSeriesByMutilThread(filePath, [14])
    # mkdir_multi('H:/python_ts/Test2')
    # mkdir_multi('H:/python_ts/Test3')
