#单元测试用例

import unittest
from business.main_model import MainModel

class  TestLogin(unittest.TestCase):

    #测试登录
    def test_login(self):
        mainpage = MainModel()
        user = mainpage.go_to_login_page()
        user.user_login('test12345678', '09090808')
        login_name=mainpage.user_name_text()
        self.assertEqual(login_name,'test12345678')

    #测试注册
    def test_register(self):
        mainpage=MainModel()
        user=mainpage.go_to_register_page()
        user.user_register('test12345678','09090808','09090808','14368601968@qq.com')

if __name__ == '__main__':
    unittest.main()