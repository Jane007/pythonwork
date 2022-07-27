# @Project : pythonwork
# @File    : test_login.py
# @Author  : zhangjing
# @Time    : 2022/7/27 10:46
# @Software : Pycharm
# @Description :
import json
from pprint import pprint

from tools.ymlController import get_yaml_data
from libs.login import Login
#1、拿数据(所有数据)
loginData = get_yaml_data("../data/loginData.yml")
#2、执行接口,获取响应数据
result = Login.login(loginData[0]);
print(result)
print(loginData[0]['resp']['success'])
#3、断言
if result['success'] == loginData[0]['resp']['success']:
    print("请求成功")


'''
需要批量运行用例，引入自动化测试框架pytest
结果用allure+log
持续集成 jenkins + gitlab
项目部署 docker

'''


