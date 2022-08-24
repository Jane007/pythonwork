# @Project : pythonwork
# @File    : test_login.py
# @Author  : zhangjing
# @Time    : 2022/7/27 10:46
# @Software : Pycharm
# @Description :
import allure
import os
import pytest as pytest

from libs.login import Login
from tools.ymlController import get_yaml_data
from vip.homework import getSalary
# #1、拿数据(所有数据)
# loginData = get_yaml_data("../data/loginData.yml")
# #2、执行接口,获取响应数据
# result = Login.login(loginData[0]);
# print(result)
# print(loginData[0]['resp']['success'])
# #3、断言
# if result['success'] == loginData[0]['resp']['success']:
#     print("请求成功")


'''
需要批量运行用例，引入自动化测试框架pytest
结果用allure+log
持续集成 jenkins + gitlab
项目部署 docker
'''
# pytest 框架自动化测试 测试规则
'''
    1、py测试文件必须以test_ 开头（或_test结尾）
    2、测试类必须以Test开头，并且不能有init方法
    3、测试方法必须以test开头
    4、断言必须使用assert
    PASSED 通过
    FAILED 用例失败

    老版本 . 成功 F 用例失败 E error 失败

'''
'''
需求：有多个用例自动执行
方案：数据驱动---读取用例数据---给框架执行
        1、用例的请求数据
        2、用例的请求期望结果
'''
# 登陆接口封装类


class TestLogin:
    # 数据驱动的方法
   # @pytest.mark.parametrize('a,b',[(1,2)])
    @pytest.mark.skip(reason="不想跑这个")
    @pytest.mark.parametrize('inData', get_yaml_data('../data/loginData.yml'))
    def test_login(self, inData):
        # print(inData)
        # 调用业务代码
        result = Login.login(inData)
        assert result['code'] == inData['resp']['code']

    @pytest.mark.login
    def test_login_online(self,login_init):
        result = login_init
        print(result)
        assert 1==1


if __name__ == '__main__':
    pytest.main(['test_login.py', '-s', '--alluredir', '../report/tmp'])
    os.system("allure serve ../report/tmp")
'''
python + allure 执行测试
1、先下载allure.zip
2、解压文件，配置bin文件到path
3、pip install alluer-pytest
4、验证

allurer 报告方案原理
    1、生成报告所需的文件
    2、使用一些工具打开可视化报告
'''


@pytest.fixture(scope="session", autouse=True)
def start_running():
    print("马上开始执行自动化测试")
    yield
    print("自动化测试开始处理垃圾")
