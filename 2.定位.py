from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 设置浏览器，启动浏览器
def she():
    # 创建设置浏览器对象
    q1 = Options()
    # 禁用沙盒模式
    q1.add_argument('--no-sandbox')
    # 保持浏览器打开状态（默认是代码执行完毕自动关闭）
    q1.add_experimental_option(name='detach', value=True)

    # 创建并启动浏览器
    a1 = webdriver.Chrome(service=Service('chromedriver.exe'), options=q1)
    return a1

# 打开网页
a1 = she()
# a1.get('https://www.baidu.com/')


# 定位元素

# 1.使用ID/Name (比较准确，因为ID是唯一的，但是不一定每个元素都有ID)
# a2 = a1.find_element(By.ID, 'kw') #类型是ID，value是kw
# a2.send_keys('python')
# a3 = a1.find_element(By.ID, 'su')
# time.sleep(2)
# a3.click() #点击按钮

# 2. 使用CLASS_NAME (不唯一，可能有多个元素)
# ①class值不能有空格，有空格意味着两个class
# ②如果有重复值，需要切片
# ③有的网站class值是动态生成的，可能会导致定位失败
a1.get('https://www.bilibili.com/')
a4 = a1.find_elements(By.CLASS_NAME, 'channel-link')[1] #切片，找到好多个这种类型的，取第二个元素，即打开电影
a4.click() #点击按钮
