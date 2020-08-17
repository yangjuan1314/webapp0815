#首页登录

from pom.base import BaseDriver
from  selenium.webdriver.common.by import By

class LoginPage(BaseDriver):
    #定义好变量
    _login_name=By.ID,'name'
    _login_pass=By.ID,'pass'
    _login_btn=By.CSS_SELECTOR,'[type="submit"]'

    #输入用户名
    @property
    def login_name(self):
        return self.driver.find_element(*self._login_name)

    #输入密码
    @property
    def login_pass(self):
        return self.driver.find_element(*self._login_pass)

    #点击登录
    @property
    def login_btn(self):
        return self.driver.find_element(*self._login_btn)