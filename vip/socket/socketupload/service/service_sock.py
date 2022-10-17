# @Project : pythonwork
# @File    : service_sock.py
# @Author  : zhangjing
# @Time    : 2022/8/18 9:32
# @Software : Pycharm
# @Description :

import socket
#创建socket容器
sk = socket.socket()
#绑定ip地址和端品号 是元组对象
sk.bind(('127.0.0.1',12001))
#监听
sk.listen()
print('服务端启动........')

def get_file(sk):
    #服务器端接收文件 1、先接收文件的大小 2 接收文件名 3 接收文件
    conn, addr = sk.accept()
    fileSize = int(str(conn.recv(1024).decode('utf8')))
    print(fileSize)
    conn.send(b'ok')
    fileName = str(conn.recv(1024).decode('utf8'))
    conn.send(b'ok')


    #读取文件

    with open('%s'%fileName,'wb') as f:
        while fileSize > 0:
            data = conn.recv(1024)
            f.write(data)
            fileSize -= 1024

    conn.close()


get_file(sk)
sk.close()


