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

a1 = she()

# 打开指定网址
a1.get('https://www.baidu.com')
time.sleep(2)

#调窗口大小
a1.maximize_window() # 最大化窗口
time.sleep(2)
a1.minimize_window() # 最小化窗口
time.sleep(2)

a1.close() # 关闭标签页
# a1.quit() # 关闭浏览器