import os
import urllib
import requests

''' http://www.yaocaiwuziyou.com/pdftest/generic/web/viewer.html?file=/Public/pdf/5c525abf0fb13.pdf
'''
pdfPath = "F:\理财\\笔记总结"


def downloadPdfBook(filePath: pdfPath, url, fileName):
    # if not os._exists(pdfPath):
    #     os.makedirs(pdfPath)
    # 目录是否存在,不存在则创建
    mkdirlambda = lambda x: os.makedirs(x) if not os.path.exists(x) else True
    mkdirlambda(pdfPath)

    pdf = requests.get(url, stream=True)

    with open(os.path.join(pdfPath, fileName + ".pdf"), "wb+") as buf:
        buf.write(pdf.content)
        buf.close()
    print("爬取完成...")


def getFile(url):
    file_name = url.split('/')[-1]
    u = urllib.request.urlopen(url)
    f = open(file_name, 'wb')

    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()
    print("Sucessful to download" + " " + file_name)

if __name__ == '__main__':
    url = "http://www.yaocaiwuziyou.com/pdftest/generic/web/viewer.html?file=/Public/pdf/5c525abf0fb13.pdf"
    filename = "第1周笔记 - 财务自由纲领（1 - 13）、太极图中财务自由智慧(1 - 2)"
    downloadPdfBook(pdfPath, url, filename)

    getFile(url)

