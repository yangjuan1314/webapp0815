#执行结果

from business.user_model import UserModel
from business.main_model import MainModel

if __name__ == '__main__':
    mainpage=MainModel()
    user=mainpage.go_to_login_page()
    user.user_login('test9',123456)