#首页登录元素定位

from selenium.webdriver.common.by import By
from pom.base import BaseDriver

class LoginPage(BaseDriver):
    _login_name = 'name'
    _login_pass = 'pass'
    _login_btn = '//div[@class="form-actions"]/input[@type="submit"]'

    @property
    def login_name(self):
        """
        登录用户名输入框
        :return:
        """
        return self.driver.find_element_by_id(self._login_name)

    @property
    def login_pass(self):
        """
        登录的密码输入框
        :return:
        """
        return self.driver.find_element_by_id(self._login_pass)

    @property
    def login_btn(self):
        """
        登录按钮
        :return:
        """
        return self.driver.find_element_by_xpath(self._login_btn)