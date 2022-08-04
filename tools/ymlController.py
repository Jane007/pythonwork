# @Project : pythonwork
# @File    : ymlController.py
# @Author  : zhangjing
# @Time    : 2022/7/27 9:18
# @Software : Pycharm
# @Description : read yaml file
# 需要引进第三方库  pip install pyYaml
import yaml
def get_yaml_data(fileDir):
    #1、获取文件    把本地磁盘文件加载到内存
    # 变量后面加空格 PEP8格式  -r 读文件
    fileObject = open(fileDir,mode='r',encoding="utf-8")
    # 2、使用yaml方法读取数据
    result = yaml.load(fileObject,Loader=yaml.FullLoader)
    return result

if __name__ == '__main__':
    # fo = get_yaml_data("../data/loginData.yml")
    # print(fo)
    x = input("请输入你想要进入的环境")
    if x == "dev":
        print("进入了开发环境")
    elif x == "test":
        print("恭喜进入了测试环境")
    else:
        print("恭喜进入了正式环境")

    input("\n\n按下 enter 键后退出。")