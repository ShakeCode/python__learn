import os
import re
import time

import requests


# 7.12
# ndN: / 90
# 后重庆美女，非洲赚钱路子野，跟总统夫人做姐妹！过上富人生活  # 海外生活 # 海外华人华侨 https://v.douyin.com/jkWRB5V/ 复制此链接，打开Dou音搜索，直接观看视频！

class AnalysisTik:

    def doAnalysis(self, paramUrl):
        print("doAnalysis  url：%s" % paramUrl)
        regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

        url = re.findall(regex, paramUrl)[0]
        print("{0}  解析最终url地址: {1}".format(paramUrl, url))
        douyin = url
        headers = self.getHeader()
        ree = requests.get(douyin, headers=headers)
        # 对页面进行重定向处理 获取新的短视频链接
        new_url = ree.url
        # print(new_url)
        # https://www.iesdouyin.com/share/video/7120194285059788073/?region=CN&mid=6607047142617910024&u_code=if86a7jd&did=MS4wLjABAAAAxWn3bFKxVOpbMG_Ocvy7YJitc49o0gG39ucM5ohabQ0&iid=MS4wLjABAAAAlbksxOcUoFf3fEpwDkkJ3hlXXS6nK-9vB7IVcSBB1XljPwr6eDOn76tKDrf90ktL&with_sec_did=1&titleType=title&timestamp=1658190604&utm_campaign=client_share&app=aweme&utm_medium=ios&tt_from=copy&utm_source=copy
        # 7120194285059788073 即为视频 id
        # 使用正则提取id
        id = re.search(r'/video/(.*?)/', new_url).group(1)

        # 提取带水印短视频链接地址
        # https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=7120194285059788073
        url = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=' + id
        ree = requests.get(url, headers=headers)
        wm = ree.json()
        # 使用正则提取无水印视频链接
        notWaterMarkerUrl = wm['item_list'][0]['video']['play_addr']['url_list'][0].replace('wm', '')
        share_title = wm['item_list'][0]['share_info']['share_title']
        print("视频标题：%s" % share_title)
        return {"notWaterMarkerUrl": notWaterMarkerUrl, "title": share_title}

    def getHeader(self):
        # 请求头使用浏览器模拟的手机端请求头
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Mobile Safari/537.36 Edg/103.0.1264.62',
            'Connection': 'close'
        }
        return headers

    def doDownLoad(self, url: str, local_save_path: str, fileName: str) -> None:
        """
        下载视频到本地目录
        :param url: 下载地址
        :param local_save_path: 本地文件保存路径 命名方式: file +filename 注意需要指定文件名，否则报错
        :return:
        """
        try:
            headers = self.getHeader()
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
            path_1 = (local_save_path + fileName + '.mp4')
            print("视频:%s  数据长度为:%s   保存文件：%s" % (url, reponse_body_lenth, path_1))

            if os.path.exists(path_1):
                print("视频已存在!")
                return

            # 保存抖音视频mp4格式，二进制读取
            # with open(path_1, "wb") as xh:
            with open((f"{local_save_path}\{fileName}.mp4"), "wb") as xh:
                # 先定义初始进度为0
                write_all = 0
                for chunk in response.iter_content(chunk_size=1000000):
                    write_all += xh.write(chunk)
                    # 打印下载进度
                    print("下载进度：%0.2d%%" % (100 * write_all / reponse_body_lenth))
                # print(f"file:{url} download success!")
        except Exception as e:
            print(f"downLoad file error,please check whether the file path is correct!\nerror massage：{e} ")
            raise e
            print("download success!")


    def doAnalysisDownLoad(self, paramUrl: str, save_path: str):
        videoMsg = self.doAnalysis(paramUrl)
        print("最终视频地址：%s" % videoMsg['notWaterMarkerUrl'])
        print("最终视频标题：%s" % videoMsg['title'])
        self.doDownLoad(videoMsg['notWaterMarkerUrl'], save_path, videoMsg['title'])


if __name__ == '__main__':
    # url = 'https://v.douyin.com/2AAVEak/'
    url = 'https://v.douyin.com/jkWRB5V/'
    obj = AnalysisTik()
    obj.doAnalysisDownLoad(url, 'D:\\')
    # 报错：Caused by SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)‘)))。也可能是开了翻墙软件的缘故，关闭翻墙软件可能就好了

    # print("下载进度：%0.2d%%" % (100 * 1 / 2))

    # reg = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    # url = re.findall(reg,
    #                  '0.71 zgo:/ 村民用愚公移山的方式 为村子开辟一条新道路 简直难以置信 # 自驾游 # vlog旅行记 # 重庆 # 巫溪 https://v.douyin.com/jBHoEyr/ 复制此链接，打开Dou音搜索，直接观看视频！')
    # print("解析最终url地址:{0}".format(url))
    #
    # url = re.findall(reg, 'https://v.douyin.com/jkWRB5V/')
    # print("解析最终url地址:{0}".format(url))

    # print(f"{1}\{2}.mp4")
