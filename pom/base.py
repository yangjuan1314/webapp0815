#初始化浏览器，
from selenium import  webdriver
import os

from selenium.webdriver.chrome.webdriver import WebDriver

#chromedriver = os.path.join(os.path.dirname(__file__),'./chromedriver.exe')
screenshot_dirs=os.path.join(os.path.dirname(__file__),'./screenshots')
if not os.path.exists(screenshot_dirs):
    os.makedirs(screenshot_dirs)

class BaseDriver:
    driver:WebDriver= None
    def __init__(self):
        if BaseDriver.driver == None:
            BaseDriver.driver = webdriver.Chrome(executable_path=r'C:\Users\许晨晨\PycharmProjects\webapp0815\chromedriver.exe')
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get("http://49.233.108.117:3000/")


class BaseUtil(BaseDriver):
    #截图方法
    @staticmethod
    def save_screenshot():
        import time
        filename=time.strftime('%Y_%m_%D_%H_%M_%S')
        filepath=os.path.join(screenshot_dirs,filename+'.png')
        print(filepath)
        BaseUtil.driver.save_screenshot(filepath)