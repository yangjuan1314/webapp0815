#初始化浏览器，
from selenium import  webdriver
import os

from selenium.webdriver.chrome.webdriver import WebDriver

#chromedriver = os.path.join(os.path.dirname(__file__),'./chromedriver.exe')

screenshots_dirs = os.path.join(os.path.dirname(__file__),'../screenshots')
if not os.path.exists(screenshots_dirs):
    os.makedirs(screenshots_dirs)


#定义浏览器类
class BaseDriver:
    driver:WebDriver= None
    def __init__(self):
        if BaseDriver.driver == None:
            BaseDriver.driver = webdriver.Chrome(executable_path=r'C:\Users\许晨晨\PycharmProjects\webapp0815\chromedriver.exe')
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get("http://49.233.108.117:3000/")


#一些操作类
class BaseUtil(BaseDriver):
    #截图方法
    @staticmethod
    def save_screenshot():
        import time
        filename = time.strftime('%Y_%m_%d_%H_%M_%S')
        filepath = os.path.join(screenshots_dirs, filename + '.png')
        BaseUtil.driver.save_screenshot(filepath)

    @staticmethod
    def max_window():
        baseutil=BaseUtil()
        baseutil.driver.maximize_window()

    @staticmethod
    def close_window():
        BaseUtil.driver.quit()