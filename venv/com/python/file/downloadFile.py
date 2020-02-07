import  requests
import  os

root="d:\\爬取淘宝图片"
# print(os.path.join(root,"test.png"))
if not os.path.exists(root):
  # 创建目录
    os.makedirs(root)
# url = 'http://g.search.alicdn.com/img/i4/31591003/TB2fJBHpOAnBKNjSZFvXXaTKXXa_!!0-saturn_solar.jpg_240x240xz.jpg_.webp'
url = 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2562313396,3549376004&fm=27&gp=0.jpg'
# url ='http://www.solarspace.co.uk/PlanetPics/Neptune/NeptuneAlt1.jpg'
# url = "http://www.oschina.net/img/logo_s2.png"
r = requests.get(url,stream=True)
# with open(os.path.join(root ,"耐克nike2.jpg.webp"), "wb") as code:
with open(os.path.join(root ,"美女.jpg"), "wb") as code:
    code.write(r.content)
    code.close()
print("爬取完成")

# url = "http://www.oschina.net/img/logo_s2.png"
# import urllib
# urllib .urlretrieve(url,root+"\\logo.png")