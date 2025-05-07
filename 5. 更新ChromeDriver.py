from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def she():
    q1 = Options()
    q1.add_argument('--no-sandbox')
    q1.add_experimental_option(name='detach', value=True)
    a1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=q1)
    return a1

a1 = she()
a1.get('https://www.baidu.com')
time.sleep(2)
a1.maximize_window() 
time.sleep(2)
a1.minimize_window() 
time.sleep(2)
a1.close()