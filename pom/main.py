#首页元素定位

from pom.base import BaseDriver
from selenium.webdriver.common.by import By

class MainPage(BaseDriver):

    #定义好首页的元素
    _login_link=By.LINK_TEXT,'登录'
    _register_link=By.LINK_TEXT,'注册'

    #注册
    @property
    def register_link(self):
        return self.driver.find_element(*self._register_link)

    #登录
    @property
    def login_link(self):
        return self.driver.find_element(*self._login_link)
