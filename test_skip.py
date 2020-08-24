"""
测试登录场景
包含
1.正常场景
2.异常场景
"""

try:
    import yaml
except ImportError:
    have_yaml_support=False
else:
    have_yaml_support=True
print(have_yaml_support)




import unittest
import os,sys

is_win32=sys.platform=='win32'     #判断操作平台是否是win32，并赋值给is_win32
needwindows=unittest.skipUnless(is_win32,'需要操作系统为win32')

class Test1(unittest.TestCase):

    def test01(self):
        assert True

    @needwindows
    def test02(self):
        assert True

    @unittest.skipIf(sys.platform=='win32','win32')
    def test03(self):
        assert True

    @unittest.skip('这次不执行')
    def test04(self):
        assert True

if __name__ == '__main__':
    unittest.main(verbosity=2)