#用户登录

from pom.login_page import LoginPage

class UserModel:
    def __init__(self):
        self.loginPage = LoginPage()

    def user_login(self,username,passwd):
        """
        使用用户名和密码进行登录
        :param username:
        :param passwd:
        :return:
        """
        self.loginPage.login_name.clear()
        self.loginPage.login_name.send_keys(username)
        self.loginPage.login_pass.clear()
        self.loginPage.login_pass.send_keys(passwd)
        self.loginPage.login_btn.click()
