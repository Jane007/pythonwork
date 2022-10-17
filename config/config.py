# @Project : pythonwork
# @File    : config.py
# @Author  : zhangjing
# @Time    : 2022/7/26 19:52
# @Software : Pycharm
# @Description :
HOST="http://192.168.100.11:8987"

ONLINE="https://app-api.xw18.cn"

TEST = "http://192.168.1.212:8987"

"""
在一些代码里使用相对路径会报文件找不到！
../data/xxxxxx
解决方案：
    通过代码自动获取当前运行项目的路径： 
"""
import os  #
print(__file__)#当前运行文件的路径
print(os.path.realpath(__file__))#当前运行文件的绝对路径
project_path =os.path.split(os.path.realpath(__file__))[0].split('configs')[0]
print(project_path)#项目路径
