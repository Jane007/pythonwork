# @Project : pythonwork
# @File    : client_sock.py
# @Author  : zhangjing
# @Time    : 2022/8/18 9:32
# @Software : Pycharm
# @Description :

import socket
import os
#创建socket容器
client = socket.socket()
#联接服务器地址端口
client.connect(('127.0.0.1',12001))
print("客服端连接上服务端，可以上传文件了")


def post_file(sk,filePath):
    fileSize = os.path.getsize(filePath)
    sk.sendall(str(fileSize).encode('utf-8'))
    a = sk.recv(1024).decode('utf-8')
    print(a)
    fileName = os.path.basename(filePath)
    sk.sendall(str(fileName).encode('utf-8'))
    b = sk.recv(1024).decode('utf-8')
    print(b)
    with open(filePath,'rb') as f:
        while fileSize > 0:
            data = f.read(1024)
            sk.sendall(data)
            fileSize -= 1024


filePath = 'E:\study\pythonwork\\vip\socket\socketupload\client\img.png'
post_file(client,filePath)
client.close()

