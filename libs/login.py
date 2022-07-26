# @Project : pythonwork
# @File    : 111.py
# @Author  : zhangjing
# @Time    : 2022/7/26 18:45
# @Description :

from config.config import HOST
import requests
# 封装一个登陆的类
class Login:
    def login(self,inData):#登陆的方法
        # url 路径
        url=f'${HOST}/application/submit'
        # 参数
        """
          data:表格数据
          json:json
          params:参数会放到url路径里 ？a=1&
          files:文件上传接口
        """
        payload=inData
        # 请求
        req = requests.post(url,payload)
        return req.text