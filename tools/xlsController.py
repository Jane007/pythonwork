# @Project : pythonwork
# @File    : xlsController.py
# @Author  : zhangjing
# @Time    : 2022/8/3 15:20
# @Software : Pycharm
# @Description :
import copy
import hashlib
import json

import xlrd2

import rsa

def get_xls_data(xpath,sheetName,case_name,*args):

    workbook = xlrd2.open_workbook(xpath)
    sheetbook = workbook.sheet_by_name(sheetName)
    col = sheetbook.col_values(2)
    reqIndex = 1
    reslutData = []

    colIdex = []  # 存放用户需要获取列名对应的列编号！
    for i in args:
        #列名在sheet第0行数据
        #通过列表的值获取对应的 下标   【】.index(值)
        colIdex.append(sheetbook.row_values(0).index(i))#获取列名对应的下标

    for one in col:
        if case_name in one :
            getColData = []
            # 5 和 6 不美观
            for c in colIdex:
                #requstBody = sheetbook.cell_value(reqIndex,c)
                #expectValue = sheetbook.cell_value(reqIndex,6)
                # print(requstBody)
                #print(type(requstBody))
                res = json.loads(sheetbook.cell(reqIndex,c).value)
                getColData.append(res)
            reslutData.append(getColData)
        reqIndex +=1
    return reslutData;



def get_md5_data(s):
    md = hashlib.md5()
    md.update(s.encode('UTF-8'))
    print(md.hexdigest())


#get_md5_data('123456')


def getRas():
    st = '11111'
    publicKey,privateKey = rsa.newkeys(1024)
    print(publicKey)
    print(privateKey)
    pwd1 = rsa.encrypt(st.encode('utf-8'),publicKey)

    print('加密后的结果：%s'%pwd1.hex())

    afterDes = rsa.decrypt(pwd1,privateKey)
    st = afterDes.decode()

    print('解密后的字符：%s'%st)

#getRas()

def is_json(str1):
    try:
        json.loads(str1)#字符串--转化--字典
    except ValueError:
        return False#不是json
    return True#就是json



def get_excel_data(excelDir, sheetName, caseName, *args,runCase=['all']):  # args -元组
    """
    :param excelDir:
    :param sheetName:
    :param caseName:
    :param args:
    :param runCase: 挑选的运行用例   默认是all

    :return:
    """
    resList = []  # 存放结果
    workBook = xlrd2.open_workbook(excelDir)  # workbook  是一个xx.xls一个文件对象
    workSheet = workBook.sheet_by_name(sheetName)
    colIdex = []#存放用户需要获取列名对应的列编号！
    #------把用户输入列名--转化成列编号！------------------
    for i in args:#遍历元组
        #列名在sheet第0行数据
        #通过列表的值获取对应的 下标   【】.index(值)
        colIdex.append(workSheet.row_values(0).index(i))#获取列名对应的下标
    #-------------------------------------------------
    #print("列名对应的下标>>> ",colIdex)
    # 5- 筛选用例
    runList = []#最后的运行列表
    if runCase[0] == 'all':#全部运行！
        runList = workSheet.col_values(0)#第一列所有的数据
    else:#如果不是all
        #  连续的 001-003
        # 不连续  001,005
        for one in runCase:#['001','004-008']
            if '-' in one:#连续的 '004-008'
                start,end = one.split('-')#获取连续用例编号的头尾
                for i in range(int(start),int(end)+1):#  for 004 005 006 007 008
                    runList.append(caseName+f'{i:0>3}')
            else:
                runList.append(caseName+f'{one:0>3}')#Login001

    idx = 0  # 行的初始值
    for one in workSheet.col_values(0):  # 对我们第一列数据进行遍历
        if caseName in one and one in runList:  # 说明这个用例是符合要求的！
            getColData = []#一定要这里 ，每一次需要初始化！
            # 读取对应的数据
            # workSheet.cell(行号，列号).value
            for num in colIdex:#[9,11]
                #workSheet.cell(idx, num).value  前提是json才行！
                #如果是json字符串 就转化成字典
                #不是就不操作
                res = workSheet.cell(idx, num).value#字符串！
                # if res[0] =='{' and res[-1] =='}':
                if is_json(res):#判定是否是json格式！
                    res = json.loads(workSheet.cell(idx, num).value)#获取单元格数据！--字符串
                getColData.append(res)#把用户需要读取的列数据 append一个列表里去
            resList.append(getColData)#获取所有符合要求的用例数据！
        idx += 1  # 行编号变化
    return resList


if __name__ == '__main__':#在里面写的代码，其他模块Import  不会运行里面的代码
    res = get_excel_data('../data/inData.xlsx', '项目列表',
                         'project', '请求参数',runCase=['all'])
    #print(res)
    for one in res:
        print(one)

#if __name__ == '__main__':
    # reslutData = get_xls_data('../data/inData.xlsx','删除客户跟进','login')
    # print(reslutData)