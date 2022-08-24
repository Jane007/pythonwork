# @Project : pythonwork
# @File    : client_socket.py
# @Author  : zhangjing
# @Time    : 2022/8/17 9:29
# @Software : Pycharm
# @Description :
import socket
#创建socket容器
client = socket.socket()
#联接服务器地址端口
client.connect(('127.0.0.1',12002))
print("联系上女神了，可以聊天了")
#发送输入的字符串以utf-8
while True:
    inputData = input(">>>")
    client.send(inputData.encode('utf-8'))
    data = client.recv(1024)
    print('女神回复：'+data.decode('utf-8'))
    if data.decode('utf8') == 'quit':
        break

client.close()
