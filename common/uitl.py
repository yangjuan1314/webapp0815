#封装
import os
from selenium import webdriver

chromedriver=os.path.join(os.path.dirname(__file__),'../chromedriver')
print(chromedriver)

class Client:

    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=chromedriver)
        self.driver.implicitly_wait(10)   #隐式等待最多10s
        self.driver.get('http://49.233.108.117:3000/signin')

    def action(self,element,**kwargs):
        ele=self.driver.find_element_by_xpath(element)
        ac=kwargs.get('action')
        if ac=='sendkeys':
            ele.send_keys(kwargs.get('value'))
        if ac=='click':
            ele.click()

if __name__ == '__main__':
    client=Client
    client.action('//input[@id="name"]',action='sendkeys',value='test9')
    client.action('//input[@id="pass"]',action='sendkeys',value='123456')
