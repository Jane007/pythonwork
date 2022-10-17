# @Project : pythonwork
# @File    : service_socket.py
# @Author  : zhangjing
# @Time    : 2022/8/17 9:29
# @Software : Pycharm
# @Description :

import socket
#创建socket容器
sk = socket.socket()
#绑定ip地址和端品号 是元组对象
sk.bind(('127.0.0.1',12000))
#监听
sk.listen()
print('服务端启动........')
conn, addr = sk.accept()
print('客户端地址:', addr)
while True:
#接受客户端发来的请求
    clientData = conn.recv(1024)
    print('客户端>>：',clientData.decode('utf8'))
    if clientData.decode('utf8') == 'quit':
        break;
    inputData = input(">>>")
    conn.send(inputData.encode('utf-8'))

conn.close()
sk.close()
