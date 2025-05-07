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
a1.get('https://www.baidu.com/')

# 定位元素
a2 = a1.find_element(By.ID, 'kw') #类型是ID，value是kw
a4 = a1.find_elements(By.CLASS_NAME, 'channel-link')[1]  #find_elements返回的是一个列表，切片，找到好多个这种类型的

#进行操作：输入框、清空输入框，按钮点击
a2.send_keys('小狗好傻') #输入框输入内容
a2.clear()#清空输入框内容
a2.click() #点击按钮

#play
time.sleep(2) #等待2秒，页面加载完成
a2 = a1.find_element(By.ID, 'kw') #类型是ID，value是kw
a2.send_keys('小狗好傻') #输入框输入内容
time.sleep(2) #等待2秒，输入完成
a2.clear() #清空输入框内容
time.sleep(2)
a2.send_keys('小鲸鱼是小狗大哥') #输入框输入内容
a2 = a1.find_element(By.ID, 'su') #类型是ID，value是su
a2.click() #点击按钮