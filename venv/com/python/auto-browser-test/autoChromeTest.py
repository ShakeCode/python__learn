from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

Chrome = Chrome()  # 启动chromedriver
Chrome.implicitly_wait(1)
Chrome.get('http://www.baidu.com')  # 打开http://www.baidu.com

# 执行代码的时候会自行去寻找chromedriver.exe(在python目录下寻找)。如果我们前面没有把它放在固定的路径下，就需要在这里指定chromedriver.exe路径
# from selenium import webdriver

# wd = webdriver.Chrome()
# wd.implicitly_wait(1)

# wd.get('https://www.baidu.com/')

# 模拟浏览器已经打开了网站的登录界面。这个时候我们需要定位到输入框、密码框以及登录按钮等。
# 这里不用担心，Selenium提供了很多种定位DOM元素的方法，各有各的特点和优势。今天就主要使用 by_xpath() 这个方法来定位元素，这个方法比较灵活方便，大部分属性都可以通过它来定位。
# 【检查】→【进入开发者模式】点击左上角的图标，再点击你要找的对象，即可得到该对象的信息。点位该对象后，右键copy它的XPath！
# button_login = wd.find_element_by_xpath('//*[@id="app"]/section/div/div/div/div[2]/form/div/div[5]/button')
# button_login = wd.find_element_by_xpath('//*[@id="s-top-loginbtn"]')
# button_login.click()

try:
    Chrome.find_element(By.XPATH, '//*[@id="s-top-loginbtn"]').click()  # 点击登录按钮
    print("点击登录")
    Chrome.find_element('//*[@id="checkin-div"]/a').click()
except:
    print("已签到")

Chrome.quit()
