# @Project : pythonwork
# @File    : base1.py
# @Author  : zhangjing
# @Time    : 2022/8/8 16:49
# @Software : Pycharm
# @Description : day01
import json
import time
if __name__ == '__main__':

    # str = 'He said : "Are you OK ?"'
    # print(str)
    # str3 = '''空山不山人
    #         但闻人语响
    # '''
    # print(str3)
    # print('A'+'B')
    # print('1'+'6')
    # print('1'*'6') 报错 can't multiply sequence by non-int of type 'str'
    # print("1"* 6) # 打印六次1

    # numstr = '3.6'
    # print(int(float(numstr)))#不能直接int转，会报错
    # num1= '3'
    # print(int(num1))

    #转义符
    # str = 'd:\\test'
    # print(str)
    # path1 = r'd:\test'
    # print(path1)
    # path1 = 'd:/test'
    # print(path1)

    #字符串 字符串的切片 [起始值:终止值:步长] 包含起始值,不包含终止值,步长默认为1
    # 字符串的切片是生成了新对象,与原对象无关
    # str = 'abcdefg'
    # print(str[:3]) # 默认从0开始
    # print(str[3:]) # 默认到结束
    # str[5]='q'    # 报错，字符串是不可变对象
    # print(str)
    # print(str[::-1])  #反转

    # 列表是可变的任意对象，可以增（append,insert,extend）删（pop,remove，del list3[0] del是这样操作的），改 （通过下标可以改）
    # listData = [1,3,"abc",1.2,"aaaa"]
    # list2 = ["ffff",1324]
    # listData.append("bbbb")
    # listData.insert(5,"ttttt")
    # listData.extend(list2)
    # listData.pop(0)
    # listData.remove("abc")
    # # print(listData)
    # listData[1]="9999"
    # print(listData)
    # print(listData[:]) # 生成一个完整的切片，是一个新对象，和原对象没有关系

    # 1,1,2,3,5,8,13,21,34 斐波那契数列
    # list1=[]
    #
    # for i in range(20):
    #     if i <= 1:
    #         list1.append(i)
    #     else :
    #         list1.append(list1[-2]+list1[-1])
    # print(list1)


    # 元组 tuple 也可以使用下标和切片  但是元组是不可变对象
    # tuple1 = (1,3)
    # print(type(tuple1))
    # tuple2 = (10,20,30)
    # tuple2[2] = 40  # 这个会报错 元组是不可变对象
    # print(tuple2[:2])


    # 浅拷贝,深拷贝
    list1= [1,20,250,[30,40]]
    # list_new = list1 # 此处实际上只是建立了list9的一个快捷方式 只要list1改值了，new 也会改
    # list1[0] = 800
    # print(list1)
    # print(list_new)

    # list9_new = copy.copy(list1) # 浅拷贝 列表是新对象，子列表仍然是相同对象
    # list1[0] = 200
    #
    # list1[-1][0] = 360
    # print(list1)
    # print(list9_new)
    # 浅拷贝等价于切片list9_new=copy.copy(list9),也可以写成list9_new=list9[:]

    # 深拷贝,列表和子列表都是不同的对象
    # list8_deepCopy = copy.deepcopy(list1)
    # list1[0] = 300
    # list1[-1][0] = 900
    # print(list8_deepCopy)
    # print(list1)

    # 字典 是无序的 update方法可以合并字典 #update 新增或修改
    # dict1 = {'A':'apple','B':'banana'}
    # dict2 = {'C':'Cat','D':'dog'}
    # print('a' in dict1)
    # dict1.update(dict2)
    # d = {**dict1,**dict2}  # 合并两个字典
    #print(id(dict1))
    # 清空字典 2235750595648
    # dict1.clear()
    # print(dict1)
    # print(id(dict1))

    # print(d)
    # for k,v in dict1.items():
    #     print(k,v)


    # str1='''{ "aac003" : "tom", "tel" : "13959687639", "crm003" : "1", "crm004" : "1" }'''
    #
    # str_new1 = json.loads(str1) #将json格式转为真正的字典
    # print(type(str_new1))
    # print(str_new1)
    # str_new2 = json.dumps(str_new1)#将字典格式转为json格式
    # print(type(str_new2))
    # print(str_new2)


    # 文件操作encoding='utf-8'
    # r+ 如果文件不存在,则报错,写入时是覆盖写入
    # w+ 如果文件不存在,则新建文件,写入时是清空写入
    # a+ 如果文件不存在,则新建文件,写入时是追加写入
    # file1 = open('../data/note.txt','a+',encoding='utf-8')
    # # print(file1.read()) # 读取文件内容
    # # print(file1.readline()) # 读取一行数据
    # file1.write("\n大家好，欢迎来到python世界")
    #
    # file1.seek(0) # 让光标回到文件开头,在文件同时进行读写时
    #
    # print(file1.read())
    # file1.close()

    # file2 = open('../data/note.txt','r',encoding='utf-8')
    # file2.seek(0)#从第几个开始读
    # print(file2.read())
    # file2.close()

    # with open 与 open 很类似，它可以处理多个文件，并且不用close（）
    # file1= '../data/note.txt'
    # file2 = '../data/note2.txt'
    # with open(file1,'r',encoding='utf-8') as f1, open(file2,'r',encoding='utf-8') as f2:
    #     print(len(f1.readlines()))
    #     print(f1.read())
    #     print(f2.read())

    # 倒计时
    for one in range(10,1,-1):
        str = f'\r倒计时开始：{one} '
        print(str,end='')   #\r让光标回到行首 ，end=''--结束符为空，即不换行
        time.sleep(1)
    else:
        print('\r倒计时结束')