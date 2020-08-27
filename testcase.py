#执行结果

# from business.user_model import UserModel
# from business.main_model import MainModel
#
# if __name__ == '__main__':
#     mainpage=MainModel()
#     user=mainpage.go_to_login_page()
#     user.user_login('test9',123456)


import unittest
from pom.base import *
from HTMLTestRunner import HTMLTestRunner

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

def runner_default():
    # 创建测试套件
    runner = unittest.TextTestRunner(verbosity=2)
    # 获取测试套件
    suite = create_test_suite()
    runner.run(suite)

def runner_html_report():
    #创建runner
    suite=create_test_suite()
    with open('report.html',mode='wb')as f:
        runner=HTMLTestRunner(stream=f,title='cndoe.js test',description='第一套测试报告')
        runner.run(suite)


if __name__ == '__main__':

    runner_html_report()
    BaseUtil.close_window()