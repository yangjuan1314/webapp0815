#单元测试用例

import unittest
from business.main_model import MainModel
from pom.base import BaseUtil

class  TestLogin(unittest.TestCase):

    def tearDown(self) -> None:
        '''
        每个testcase执行完后的操作
        :return:
        '''
        BaseUtil.save_screenshot()

    # #测试登录
    # def test_login(self):
    #     mainpage = MainModel()
    #     user = mainpage.go_to_login_page()
    #     user.user_login('test9', '123456')
    #     login_name=mainpage.user_name_text()
    #     self.assertEqual(login_name,'test9')

    #测试注册
    def test_register(self):
        mainpage=MainModel()
        user=mainpage.go_to_register_page()
        user.user_register('test12345678','09090808','09090808','14368601968@qq.com')
        register_result=user.get_register_result()
        self.assertEqual(register_result,'用户名或邮箱已被使用。')

if __name__ == '__main__':
    unittest.main()