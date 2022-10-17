# @Project : pythonwork
# @File    : test_base.py
# @Author  : zhangjing
# @Time    : 2022/9/19 11:42
# @Software : Pycharm
# @Description :
import statistics
import yaml

class OperatorYml():
    def readYml(self,filePath):
        with open(filePath,mode="r",encoding="utf-8") as f:
            load = yaml.load(f,Loader=yaml.FullLoader)
            return load



rest = OperatorYml().readYml("data.yml")

#print(rest)

content = [rest[key]  for key in dict.keys(rest)]
re = []

# list1 = content[0]
# list2 = content[1]
# z = list(zip(list1,list2))
# print(z)

# print(content[0][0],content[1][0])
# print(content[0][1],content[1][1])
# print(content[0][2],content[1][2])

for i in range(len(content[0])):
    re2 =[]
    for j in range(len(content)):
        re2.append(content[j][i])
        #re2.append(content[j][i])
    re.append(re2)
#print(re)

a = [1,2,3]
b = [4,5,6]
c = [7,8,9,10,11]


a_b = zip(a,b)
# zip()之后的结果只能“使用一次”
# zip()实际上是一个生成器对象，故使用list()获取zip()结果时，已经相当于是完成一次迭代遍历

#print(list(a_b))

# 第二次再次使用list()时迭代已经结束，所以返回[] 如果要多次使用，用一个变量接收即可
#print(list(a_b))

ab = list(zip(a,b))
# print(ab)
# print(ab)

#以短的为准
ac = zip(a, c)
#print(list(ac))

# *与 zip 相反，可理解为解压，返回二维矩阵式
_ac = zip(*ac)
#print(list(_ac))

q = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]], map()函数把zip(*a)后的每一个元素转化为list
print(list(map(list,zip(*q))))
#print(list(zip(*q)))
#print(list(map(list, zip(*q))))


def test_param(locate):
    print(*locate)

test_param(['css selector','table[id^="DataTables_Table"] tbody td:nth-child(2)'])