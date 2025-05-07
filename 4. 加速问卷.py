from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

option=Options()
option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_experimental_option('useAutomationExtension',False)
option.add_experimental_option(name='detach', value=True)

    # 创建并启动浏览器
a1 = webdriver.Chrome(service=Service('chromedriver.exe'), options=option)
a1.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',{'source':'Object.defineProperty(navigator,"webdriver",{get:()=>undefined})'})
a1.get('https://www.wjx.cn/vm/tIvrtIF.aspx#')


# 定位元素

# 1.使用ID/Name (比较准确，因为ID是唯一的，但是不一定每个元素都有ID)
a2 = a1.find_elements(By.CLASS_NAME, 'ui-radio')[1] #类型是ID，value是kw
a2.click()
print(1)
a3 = a1.find_element(By.ID, 'q3')
print(2)
a3.send_keys('我是小狗')
# print(4)
a4 = a1.find_element(By.ID, 'ctlNext')
print(5)
# time.sleep(2)
a4.click() #点击按钮
print("success")
# a2.send_keys('python')
# a3 = a1.find_element(By.ID, 'su')
# time.sleep(2)
# a3.click() #点击按钮

time.sleep(0.2)
confirm = a1.find_element(By.ID, 'captchaOut')
confirm.click()
print("successful!!!")