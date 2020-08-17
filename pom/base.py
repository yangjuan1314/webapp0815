#初始化浏览器，
from selenium import  webdriver
import os

from selenium.webdriver.chrome.webdriver import WebDriver

#chromedriver = os.path.join(os.path.dirname(__file__),'./chromedriver.exe')

class BaseDriver:
    driver:WebDriver= None
    def __init__(self):
        if BaseDriver.driver == None:
            BaseDriver.driver = webdriver.Chrome(executable_path=r'C:\Users\许晨晨\PycharmProjects\webapp0815\chromedriver.exe')
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get("http://49.233.108.117:3000/")