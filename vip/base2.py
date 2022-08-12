# @Project : pythonwork
# @File    : base2.py
# @Author  : zhangjing
# @Time    : 2022/8/11 11:10
# @Software : Pycharm
# @Description :


import os
import sys
#os.system('calc')#调用操作系统的计算器
#os.system('cmd')
#运程连接桌面
#os.system('mstsc')

#系统环境变量path内容
#print(sys.path)

#列表推导式
#print(len([i for i in range(100001)  if '3' in str(i)]))
#print([i for i in range(100001)  if '3' in str(i)])


list2 = [23, -1, 6, 92, 128, -99, 50, 36]

for i in range(len(list2)-1):
    for j in range(len(list2)-1-i):
        if list2[j] > list2[j+1]:
            # temp = list2[j]
            # list2[j] = list2[j+1]
            # list2[j+1] = temp
            list2[j],list2[j+1] =  list2[j+1],list2[j]


#print(list2)


log = '''
f20180111014341/i_51a7hC3W.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156063244230469	image/jpeg	0	
f20180111014341/j_R0Hpl4EG.json	1036	ForGzwzV3e-uR3_UzvppJs1VgfQG	15156064773253144	application/json	0	
f20180111020739/i_0TDKs0rD.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156076847077556	image/jpeg	0	
f20180111020739/j_JFO6xiir.json	1040	FmUhTchdLOd7LBoE8OXzPLDKcW60	15156077904192983	application/json	0	
f20180111090619/i_1BwNksbL.jpg	49634	FtXBGmipcDha-67WQgGQR5shEBu2	15156329458714950	image/jpeg	0	
f20180111090619/i_3BKlsRaZ.jpg	30152	FoWfMSuqz4TEQl5FT-FY5wqu5NGf	15156330575626044	image/jpeg	0	'''


listData = log.strip().split('\n');
listDic = {}
for one in listData:
    line = one.split('\t')
    image = line[0].split('.')
    if len(image)>0:
        key = image[1]
        val = int(line[1])
        if key in listDic:
            old = listDic[key]
            listDic[key] = int(old)+val
        else:
            listDic[key] = val
    # image = one.split('.')
    # print(image)


print(listDic)