#执行结果

# from business.user_model import UserModel
# from business.main_model import MainModel
#
# if __name__ == '__main__':
#     mainpage=MainModel()
#     user=mainpage.go_to_login_page()
#     user.user_login('test9',123456)


import unittest

def create_test_suite():
    #测试套件
    suite=unittest.TestSuite()
    #测试用例加载器
    loader=unittest.TestLoader()
    #搜索所有的测试用例
    alltests=loader.discover(start_dir='testcases',pattern='test**.py')
    #测试套件添加测试用例
    suite.addTests(alltests)
    return suite

if __name__ == '__main__':
    #创建测试套件
    runner=unittest.TextTestRunner(verbosity=2)
    #获取测试套件
    suite=create_test_suite()
    runner.run(suite)




