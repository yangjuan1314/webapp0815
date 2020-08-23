#用户登录

from pom.main import MainPage
from business.user_model import UserModel

class MainModel:

    def __init__(self):
        self.mainPage = MainPage()
        self.userModel = UserModel()

    def go_to_login_page(self):
        """
        跳转到登陆页面
        :return:
        """
        self.mainPage.login_link.click()
        return self.userModel

    def user_name_text(self):
        '''
        获取用户的文本值
        :return:
        '''
        return self.mainPage.user_login_name.text