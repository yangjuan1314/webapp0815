import unittest
from ddt import ddt,data,unpack,file_data
from business.main_model import MainModel
import csv,os

logincsv = os.path.join(os.path.dirname(__file__),'../data/login.csv')

# test_csv_data= []
# with open(logincsv) as f:
#     reader = csv.DictReader(f)
#     for line in reader:
#         print(line)
#         test_csv_data.append(line)

#  [{'username': 'test10', 'passwd': "''"},{'username': 'test10', 'passwd': '123456'},{'username': "''", 'passwd': '123456'}]

# 定义test类<必须继承 unittest.TestCase>
from pom.base import BaseUtil

@ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        """每一个testcase 执行之前的操作"""
        pass


    def tearDown(self) -> None:
        """ 每一个testcase 执行完成之后的操作"""
        BaseUtil.save_screenshot()


    @classmethod
    def setUpClass(cls) -> None:
        """整个类运行执行前操作"""
        main = MainModel()
        cls.user = main.go_to_login_page()
    @classmethod
    def tearDownClass(cls) -> None:
        BaseUtil.driver.delete_all_cookies()
        BaseUtil.driver.get('http://49.233.108.117:3000/')
    # 测试方法  test开头

    @unpack
    @data(('test1','123456'),('',''),('test1',''),('','123456'))
    def test_login(self,name,passwd):

        self.user.user_login(name, passwd)

        # login_name = main.user_name_text
        # self.assertEqual(login_name,'test10')

    # @unittest.skip('No')
    # @file_data('../data/login.json')
    # def test_login_json(self,loginname, passwd):
    #     self.user.user_login(loginname, passwd)
    #
    # @unittest.skip('No')
    # @file_data('../data/login.yaml')
    # def test_login_yaml(self,loginname, passwd):
    #     self.user.user_login(loginname, passwd)
    #
    # @unpack
    # @data(*test_csv_data)
    # def test_login_csv(self,username,passwd):
    #     self.user.user_login(username, passwd)

if __name__ == '__main__':
    unittest.main(verbosity=2)