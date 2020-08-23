#单元测试用例

import unittest
from business.main_model import MainModel

class  TestLogin(unittest.TestCase):
    #测试方法
    def test_login(self):
        mainpage = MainModel()
        user = mainpage.go_to_login_page()
        user.user_login('test9', 123456)
        login_name=mainpage.user_name_text()
        self.assertEqual(login_name,'test9')

if __name__ == '__main__':
    unittest.main()