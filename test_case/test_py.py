# @Project : pythonwork
# @File    : test_py.py
# @Author  : zhangjing
# @Time    : 2022/8/4 17:38
# @Software : Pycharm
# @Description :

def test_input():
    x = input("请输入你想要进入的环境")
    if x == "dev":
        print("进入了开发环境")
    elif x == "test":
        print("恭喜进入了测试环境")
    else:
        print("恭喜进入了正式环境")

if __name__ == '__main__':
    test_input()