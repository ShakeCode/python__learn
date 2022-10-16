import json
import re
from bs4 import BeautifulSoup
import json
import re

from bs4 import BeautifulSoup

# 此处模拟获取到的html的text
response_html_str = """
        <!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>
            <script>
                var indData = [{"No": 1, "Status": "A", "Date": "Dec 17, 2004 12:00:00 AM", "Desc": "Dealing in abc", "raCate": null}];
                <!-- 后面接一大堆js函数，巴拉巴拉巴拉...  -->
                function getResultsCount(){
                    return "1";
                }
            </script>
        </body>
        </html>
    """

soup = BeautifulSoup(response_html_str, "html.parser")
"""
#compile中的正则
    1."var indData ="表示我们需要开始截取的地方
    2."(.*?)"表示中间为任意字符串
    3.";$"表示第一个；结尾的地方结束
    4."re.MULTILINE",影响^与$ 锚点匹配的位置。
      没有开关，^并且$仅在整个文本的开头和结尾处匹配。使用该开关，它们也将在换行符之前或之后匹配
    5."re.DOTALL",re.DOTALL,影响.模式可以匹配的内容。
      如果没有切换，则.匹配除换行符之外的任何字符。通过该开关，换行符也将匹配
"""

pattern = re.compile(r"var indData =(.*?);$", re.MULTILINE | re.DOTALL)
script = soup.find('script', text=pattern)
data_str = pattern.search(script.text).group(1)
data_json = json.loads(data_str, strict=False)

print(data_json)
