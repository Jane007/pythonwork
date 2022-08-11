# @Project : pythonwork
# @File    : xlsController.py
# @Author  : zhangjing
# @Time    : 2022/8/3 15:20
# @Software : Pycharm
# @Description :
import copy
import json

import xlrd2

def get_xls_data(xpath,sheetName,case_name):

    workbook = xlrd2.open_workbook(xpath)
    sheetbook = workbook.sheet_by_name(sheetName)
    col = sheetbook.col_values(2)
    reqIndex = 1
    reslutData = []
    for one in col:
        if case_name in one :
            requstBody = sheetbook.cell_value(reqIndex,5)
            expectValue = sheetbook.cell_value(reqIndex,6)
           # print(requstBody)
            #print(type(requstBody))
            reslutData.append((json.loads(requstBody),json.loads(expectValue)))
            reqIndex +=1
    return reslutData;

if __name__ == '__main__':
    reslutData = get_xls_data('../data/inData.xlsx','删除客户跟进','login')
    print(reslutData)