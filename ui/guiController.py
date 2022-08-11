# @Project : pythonwork
# @File    : guiController.py
# @Author  : zhangjing
# @Time    : 2022/8/5 15:18
# @Software : Pycharm
# @Description :gui 登陆功能实现

from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile
#python ui文件
from PySide2.QtUiTools import QUiLoader
import sys
# 创建一个app
app = QApplication(sys.argv)

# 打开ui界面
qfile = QFile('login.ui')
qfile.open(QFile.ReadOnly)
# 加载ui里面组件对象
ui = QUiLoader().load(qfile)
# 9 关闭文件
qfile.close()
###  =========后台实现 交互逻辑  =======

def login():
    username = ui.username.text()
    print("用户名是===》",username)
    password = ui.password.text();
    print("密码是：===》", password)
    if username == 'zhang' and password == '123':
        ui.textBrowser.append('恭喜登陆成功')
    else:
        ui.textBrowser.append('用户名密码错误，请重新输入')


###  =========后台实现 交互逻辑  =======
### 触发事件
ui.pushButton.clicked.connect(login)
# 10 ui 界面显示
ui.show()

#11 app 执行
app.exec_()





