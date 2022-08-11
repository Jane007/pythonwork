# @Project : pythonwork
# @File    : homework.py
# @Author  : zhangjing
# @Time    : 2022/8/8 16:50
# @Software : Pycharm
# @Description :

'''
写一个号段筛选程序,需求如下:
用户控制台输入一个手机号，
判断出运营商(移动（假设号段是130-150）、
联通（假设是151-170）、电信（假设是171-199）),
如果用户输入的位数不对，提示用户位数有误;如果用户输入非数字，提示有非法字符
'''

def printMobile():
    str = input('请输入：')
    flag = str.isdigit()
    print(flag)
    if len(str) != 11:
        print("手机号长度是11位，请重新输入")
        str = input('请输入：')
    elif not flag:
        print("有非法字符,请重新输入")
        str = input('请输入：')

    three = int(str[:3])
    if 130 < three <= 150:
        print("你的手机号码运营商是移动")
    elif 151 <= three <= 170:
        print("你的手机号码运营商是联通")
    elif 171 <= three <= 199:
        print("你的手机号码运营商是电信")


def getName(str):
    st = str.split(',')
    for s in st:
        if s.__contains__("the name is"):
            return  s.split("the name is")[1]

def formatstr():
    # 补齐 %ns n是任意自然数,不足n位时,补齐到n位 数字前面0补齐
    info = '我叫%6s,今年%02d岁，今年是%4d年'%('张晶',8,2022)
    print(info)
    #补齐 {:n},不足n位,则补空格.字符串默认左对齐,空格在右侧,数字默认右对齐,空格在左侧
    str = 'my name is {:20},age is {:10}'.format('zhangjing',10)
    print(str)
    # 可以改变默认的对齐方式 > 右对齐 < 左对齐 ^ 居中对齐
    str = 'my name is {:15},age is {:<10}'.format('zhangjing', 10)
    print(str)


def putInfoToDict2(fileName):
    file1 = open(fileName,'r',encoding='utf-8')
    bigDic = {}
    for line in file1.readlines():
        data = line
        #print(type(data))
        if len(data)>0:
            temp = data.replace('(', '').replace('),', '').replace('\n','').replace(');','').replace('\'','').strip()
            d = temp.split(",")
            #print(d)
            key = int(d[2].strip())
            dic = {'lessonid':int(d[1]),'checkintime':d[0]}
            if key not in bigDic:
                bigDic[key] = []
            bigDic[key].append(dic)


    return bigDic


def putInfoToDict(fileName):
    retDict = {}
    with open(fileName) as f:
        lines = f.read().splitlines()

        for line in lines:
            # remove '(' and ')'
            line = line.replace('(', '').replace(')', '').replace(';', '').strip()

            parts = line.split(',')
            ciTime = parts[0].strip().replace("'", '')
            lessonid = int(parts[1].strip())

            userid = int(parts[2].strip())

            toAdd = {'lessonid': lessonid, 'checkintime': ciTime}

            if userid not in retDict:
                retDict[userid] = []
            retDict[userid].append(toAdd)

            # or just
            # retDict.setdefault(userid,[]).append(toAdd)

    return retDict

#name: Jack   ;    salary:  12000
#name: Jack   ;    salary:  12000 ;  tax: 1200 ; income:  10800
def getSalary(file1,file2):
    with open(file1,'r',encoding='utf-8') as f1,open(file2,'a+',encoding='utf-8') as f2:
        for line in f1.readlines():
            l1 = line.split(';')
            name = l1[0].split(':')[1].strip()
            salary = int(l1[1].split(':')[1])
            tax = int(salary * 0.1)
            income = int(salary-tax)
            str = 'name: {:<8},\t salary:{:<8};\t tax:{:<8};\t income:{:>} \n'.format(name,salary,tax,income)
            f2.write(str)






if __name__ == '__main__':


    # printMobile()
    # print(3+(True+True))

    # name = getName("A pretty boy come in, the name is Patrick, level 194")
    # print(name)
    # formatstr()

    # listData = putInfoToDict2('../data/0005.txt')
    # print(listData)

    #getSalary("../data/f1.txt", "../data/f2.txt")

    # str = '我叫：{2},今年{1}岁，想去{0}玩'.format('张晶',18,'新加坡')
    # print(str)

    str = '我叫%-8s,今年%6d岁，想去%s玩'%('张晶',18,'新加坡')
    print(str)
