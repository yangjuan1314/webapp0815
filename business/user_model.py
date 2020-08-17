#用户登录

from pom.login_page import LoginPage

class UserModel:

    def __init__(self):
        self.loginpage=LoginPage

    #使用用户名与密码登录
    def user_login(self,username,userpass):
        self.loginpage.login_name.send_keys(username)
        self.loginpage.login_pass.send_keys(userpass)
        self.loginpage.login_btn.click()
