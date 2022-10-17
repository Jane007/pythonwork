# @Project : pythonwork
# @File    : run.py.py
# @Author  : zhangjing
# @Time    : 2022/9/23 10:24
# @Software : Pycharm
# @Description :
import os

if __name__ == '__main__':
    os.system("robot --listener allure_robotframework demo_baidu.robot")
    os.system('allure serve output/allure ')