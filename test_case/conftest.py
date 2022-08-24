# @Project : pythonwork
# @File    : conftest.py
# @Author  : zhangjing
# @Time    : 2022/7/27 15:35
# @Software : Pycharm
# @Description :
import pytest

# 自动化执行前的一个环境初始化操作
from config.config import HOST, ONLINE,TEST
from libs.login import Login
from libs.project import Project


URL = TEST

@pytest.fixture(scope="session",autouse=True)
def start_running():
    print("马上开始执行自动化测试")
    yield
    print("自动化测试开始处理垃圾")



@pytest.fixture(scope="class")
def sayHello():
    print("say Hello")
    yield
    print("say Hello222")



@pytest.fixture(scope="class")
def sayByBy():
    print("\n class 前置")
    print("say ByeBye")
    return 'ByeBye'

@pytest.fixture(scope='function')
def my_fixture():
    print('\n function 前置')
    yield
    print('\n function 后置')

params = [11,22,33]
ids = ['case{}'.format(i) for i in range(len(params))]
@pytest.fixture(params=params,ids = ids)
def my_fixture_id(request):
   yield request.param




@pytest.fixture(scope='class')
def login_init():
    url=f'{URL}/user/login'
    token = Login(url).login_online({'mobile': '18926078113', 'password': 'test2022'})
    return token

@pytest.fixture(scope='class')
def project_init(login_init):
    url =f'{URL}/element/projects'
    projectObject = Project(login_init,url)
    return projectObject

@pytest.fixture(scope='function')
def project_update_init(project_init):
    url = f'{URL}/element/project/350'
    # 上传文件
    return url,project_init





