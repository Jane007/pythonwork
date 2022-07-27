# @Project : pythonwork
# @File    : config_test.py
# @Author  : zhangjing
# @Time    : 2022/7/27 15:35
# @Software : Pycharm
# @Description :
import pytest
# 自动化执行前的一个环境初始化操作
@pytest.fixture(scope="session",autouse=True)
def start_running():
    print("马上开始执行自动化测试")
    yield
    print("自动化测试开始处理垃圾")
