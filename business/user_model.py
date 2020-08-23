#用户登录

from pom.login_page import LoginPage
from pom.register_page import RegisterPage

class UserModel:
    def __init__(self):
        self.loginPage = LoginPage()
        self.registerPage=RegisterPage()

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


    def user_register(self,username,passwd,repasswd,email):
        '''
        使用用户名、密码、确认密码、邮箱进行登录
        :param username:
        :param passwd:
        :param repasswd:
        :param email:
        :return:
        '''
        self.registerPage.register_name.clear()
        self.registerPage.register_name.send_keys(username)

        self.registerPage.register_pass.clear()
        self.registerPage.register_pass.send_keys(passwd)

        self.registerPage.register_repass.clear()
        self.registerPage.register_repass.send_keys(repasswd)

        self.registerPage.register_eamil.clear()
        self.registerPage.register_eamil.send_keys(email)

        self.registerPage.register_btn.click()

    def get_register_result(self,is_success=False):
        if not is_success:
            return self.registerPage.register_error_result.text
        else:
            return self.registerPage.register_success_result.text
