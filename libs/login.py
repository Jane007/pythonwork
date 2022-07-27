# @Project : pythonwork
# @File    : 111.py
# @Author  : zhangjing
# @Time    : 2022/7/26 18:45
# @Description :
import json

from config.config import HOST
from tools.ymlController import get_yaml_data
import requests
# 封装一个登陆的类
class Login:
    def login(inData):#登陆的方法
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
        return req.json()

# 快捷键 ctrl+j

if __name__ == '__main__':
    data=get_yaml_data("../data/loginData.yml")
    # content = data[0]['content']
    # content['sessionId']=data[0]['sessionId']
    # content['id'] = data[0]['id']
    # data = json.dumps(data)
    # print(data)
    res = Login.login(inData=data[0])
    print(res)