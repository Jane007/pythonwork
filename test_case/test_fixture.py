# @Project : pythonwork
# @File    : test_fixture.py
# @Author  : zhangjing
# @Time    : 2022/8/23 15:27
# @Software : Pycharm
# @Description :
import pytest


class Test_Fix:

    def test_01(self,sayByBy):
        print(sayByBy)
        print("test_01执行-->")
        assert 1==1

    def test_02(self,my_fixture_id):
        print("--->test_02执行{}".format(my_fixture_id))
        assert 1==1

    def test_03(self,sayByBy):
        print(sayByBy)
        print("test_03执行")
        assert 1==1

    def test_04(self, my_fixture):
        print("test_04执行")
        assert 1 == 1



if __name__ == '__main__':
    pytest.main(['test_fixture.py','-s'])

