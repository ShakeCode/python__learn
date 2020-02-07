import  requests
from bs4 import BeautifulSoup
# resopnseBody  = requests.get("https://wwww.baidu.com")
resopnseBody  = requests.get("http://ai.taobao.com/search/index.htm?pid=mm_10011550_0_0&unid=&source_id=search&key=%E8%B7%91%E6%AD%A5%E9%9E%8B&b=sousuo_ssk&prepvid=200_10.103.34.56_359_1436873985318&spm=a231o.7076277.1998559105.1")
# print(resopnseBody.status_code)
result = resopnseBody.text.encode(encoding="utf-8")
# print(result)

soup = BeautifulSoup(resopnseBody.text, "html.parser")
print(soup.find('body').children)
print("-----------------------解析dom...befin")
# for x in  iter(soup.find('body').children):
#     print(x)
print(soup.prettify())
print("-----------------------解析dom...end")
# for s in soup.find_all(attrs={'class':'tag'}):
for s in soup.find_all('a'):
    print(s)



