#注册页面元素

from pom.base import BaseDriver

class RegisterPage(BaseDriver):
    '''实现注册页面的封装'''
    _register_name='//input[@id="loginname"]'
    _register_pass='//input[@id="pass"]'
    _register_repass='//input[@id="re_pass"]'
    _register_email='//input[@id="email"]'
    _register_btn='//input[@type="submit"]'


    @property
    def register_name(self):
        '''
        输入注册的用户名
        :return:
        '''
        return self.driver.find_element_by_xpath(self._register_name)

    @property
    def register_pass(self):
        '''
        输入注册的密码
        :return:
        '''
        return self.driver.find_element_by_xpath(self._register_pass)

    @property
    def register_repass(self):
        '''
        输入注册的重复密码
        :return:
        '''
        return  self.driver.find_element_by_xpath(self._register_repass)

    @property
    def register_eamil(self):
        '''
        输入注册的邮箱
        :return:
        '''
        return self.driver.find_element_by_xpath(self._register_email)

    @property
    def register_btn(self):
        '''
        点击注册按钮
        :return:
        '''
        return self.driver.find_element_by_xpath(self._register_btn)


