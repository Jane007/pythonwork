# @Project : pythonwork
# @File    : project.py
# @Author  : zhangjing
# @Time    : 2022/8/24 13:34
# @Software : Pycharm
# @Description :
import pytest
import requests


class Project:
    def __init__(self,inToken,url):
        self.heard = {"Authorization" : inToken}
        self.url = url


    def project_list(self,inData):
        payload = inData
        result = requests.get(self.url,params=payload,headers=self.heard)
        return result.json()

