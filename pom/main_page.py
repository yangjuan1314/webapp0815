#首页登录元素定位

from pom.base import BaseDriver
from selenium.webdriver.common.by import By

class MainPage(BaseDriver):

    #定义好首页的元素
    _login_link='//ul[@class="nav pull-right"]/li[6]'      #登录按钮
    _register_link='//ul[@class="nav pull-right"]/li[5]'   #注册按钮
    _user_login_name='//span[@class="user_name"]/a[@class="dark"]'   #登录后的用户名


    #注册
    @property
    def register_link(self):
        return self.driver.find_element_by_xpath(self._register_link)

    #登录
    @property
    def login_link(self):
        return self.driver.find_element_by_xpath(self._login_link)

    #获取登录后的用户名
    @property
    def user_login_name(self):
        return self.driver.find_element_by_xpath(self._user_login_name)