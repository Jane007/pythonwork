# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 简单的po模式.py
# @ide     : PyCharm
# @time    : 2021/4/26 21:31

from selenium import webdriver


class LoginPage:
    def __init__(self):
        # 创建 driver 对象
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(5)
        # 最大化窗口
        self.driver.maximize_window()
        # 访问网址
        self.driver.get("http://120.55.190.222:38090/#/login")

    # 用户名输入框
    def username_input_box(self):
        return self.driver.find_element_by_id("username")

    # 密码输入框
    def password_input_box(self):
        return self.driver.find_element_by_id("password")

    # 登录按钮
    def login_button_box(self):
        return self.driver.find_element_by_id("btnLogin")


class LoginPageAction(LoginPage):

    def login_action(self):
        self.username_input_box().send_keys("松勤老师")
        self.password_input_box().send_keys("123456")
        self.login_button_box().click()


loginPageActionObj = LoginPageAction()

if __name__ == '__main__':
    loginPageActionObj.login_action()
