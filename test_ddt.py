#使用data 装饰器生成测试数据

from  ddt import ddt,data,unpack
import unittest
import random

def get_random_data():
    return random.random()


@ddt
class TestDDT(unittest.TestCase):

    def testcase01(self):
        assert True

    @data(1,10,11,12)
    def test_01(self,value):
        print(value)
        self.assertTrue(value>2)

    @data(get_random_data(),get_random_data())
    def test_02(self,value):
        print(value)
        self.assertTrue(value>2)

    @data((1,2),(2,3))
    def test_03(self, value):
        print(value)

    @unpack
    @data(('test1','123456'),('','123456'),('test1',''),('',''))
    def test_04(self,loginname,passwd):
        print(f'loginname:{loginname},passwd:{passwd}')

if __name__ == '__main__':
    unittest.main(verbosity=2)
