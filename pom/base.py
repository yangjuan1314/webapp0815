#初始化浏览器，

from selenium import webdriver
import os
from selenium.webdriver.chrome.webdriver import WebDriver

chromedriver=os.path.join(os.path.dirname(__file__),'./chromedriver.exe')
print(chromedriver)

class BaseDriver:
    driver:webdriver=None
    def __init__(self):
        if BaseDriver.driver == None:
            BaseDriver.driver = webdriver.Chrome(executable_path=chromedriver)
            self.driver.implictly_wait(10)
            self.driver.get('http://49.233.108.117:3000/')