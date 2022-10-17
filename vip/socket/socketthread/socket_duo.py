# @Project : pythonwork
# @File    : socket_duo.py
# @Author  : zhangjing
# @Time    : 2022/8/18 11:14
# @Software : Pycharm
# @Description :

import socket
import socketserver

class MySocketHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            print("女神空闲了。。。。。")
            self.data = self.request.recv(1024).decode('utf-8').strip()
            print('收到消息>>>'+self.data)
            if not self.data:
                break
            send_back = input(">>>>")
            self.request.sendall(send_back.encode('utf-8'))


host = '127.0.0.1'
port = 12002

services = socketserver.ThreadingTCPServer((host,port),MySocketHandler)
services.serve_forever()