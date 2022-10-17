# @Project : pythonwork
# @File    : hw8.py
# @Author  : zhangjing
# @Time    : 2022/8/12 17:00
# @Software : Pycharm
# @Description : 第九次思考题 动物园小游戏
'''
动物园里面有10个房间，房间号从1 到 10。
每个房间里面可能是体重200斤的老虎或者体重100斤的羊。
游戏开始后，系统随机在10个房间中放入老虎或者羊。
然后随机给出房间号，要求游戏者选择敲门还是喂食。

如果选择喂食：
喂老虎应该输入单词 meat，喂羊应该输入单词 grass
喂对了，体重加10斤。 喂错了，体重减少10斤
如果选择敲门：
敲房间的门，里面的动物会叫，老虎叫会显示 ‘Wow !!’,羊叫会显示 ‘mie~~’。 动物每叫一次体重减5斤。
游戏者强记每个房间的动物是什么，以便不需要敲门就可以喂正确的食物。
游戏3分钟结束后，显示每个房间的动物和它们的体重。
实现过程中，有什么问题，请通过课堂上讲解的调试方法，尽量自己发现错误原因。
'''
import random
import time


class Tiger:
    def __init__(self):
        self.weight = 200
        self.name = 'tiger'
        self.voise = 'WoW!!'
        self.food = 'meat'

    def roar(self):
        self.weight -= 5
        print(f'{self.name} 叫一声，减五斤')

    def feed(self,food):
        if food == self.food:
            self.weight += 10
            print('吃多了，胖十斤')
        else:
            self.weight -= 10
            print('吃错了，减十斤')


class Sheep:
    def __init__(self):
        self.weight = 200
        self.name = 'sheep'
        self.voise = 'meimei'
        self.food = 'grass'
    def feed(self,food):
        if food == self.food:
            self.weight += 10
            print('吃多了，胖十斤')
        else:
            self.weight -= 10
            print('吃错了，减十斤')

    def roar(self):
        self.weight -= 5
        print(f'{self.name} 叫一声，减五斤')


class Room:
    def __init__(self,roomNo,animal):
        self.roomNo = roomNo
        self.animal = animal



rooms = []
for i in range(1,11):
    if random.randint(0,1):
        animal = Tiger()
    else:
        animal = Sheep()
    room = Room(i,animal)
    #print(i,animal.name)
    rooms.append(room)


starttime = time.time()
while True:
    endTime = time.time()
    if endTime - starttime >= 30:
        for room in rooms:
            print(room.roomNo,room.animal.name,room.animal.weight)
        break


    roomNo = random.randint(1,11)

    rom= rooms[roomNo-1]


    # 程序运行逻辑
    str = input(f'请选择是否敲{roomNo}号门？1/2:')
    if str == '1':
        rom.animal.roar()
        #调用叫方法
    #调用喂食
    str = input(f'请输入喂的食物：')
    rom.animal.feed(str.strip())











