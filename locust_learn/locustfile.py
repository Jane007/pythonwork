# @Project : pythonwork
# @File    : locustfile.py
# @Author  : zhangjing
# @Time    : 2022/10/8 17:04
# @Software : Pycharm
# @Description :
from locust import HttpUser,task,between

class HelloUser(HttpUser):
    wait_time = between(1,5)
    @task
    def hello_world(self):
        self.client.get("/list")
        self.client.get("/")
        # self.client.get("/hello")
        # self.client.get("/world")