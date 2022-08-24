# @Project : pythonwork
# @File    : 111.py
# @Author  : zhangjing
# @Time    : 2022/7/26 18:45
# @Description :
import json

import pytest

from config.config import HOST
from tools.ymlController import get_yaml_data
import requests
# 封装一个登陆的类
class Login:
    def __init__(self,url):
        self.url = url
    def login(inData,getSession=False):#登陆的方法
        # url 路径
        url=f'{HOST}/application/submit'
        # 参数
        """
          data:表格数据
          json:json
          params:参数会放到url路径里 ？a=1&
          files:文件上传接口
        """
        payload=inData
        # 请求
        req = requests.post(url,json=payload)
        if getSession:
            return req.json()['sessionId']
        return req.json()

    def login_online(self,inData):
        payload = inData
        req = requests.post(self.url, json=payload)
        token = 'Bearer {}'.format(req.json()['token'])
        return token


# 快捷键 ctrl+j

if __name__ == '__main__':
    data=get_yaml_data("../data/loginData.yml")
    # content = data[0]['content']
    # content['sessionId']=data[0]['sessionId']
    # content['id'] = data[0]['id']
    # data = json.dumps(data)
    print(data)
    res = Login.login(inData=data[0])
    print(res)