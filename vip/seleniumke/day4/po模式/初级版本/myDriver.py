# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : myDriver.py
# @ide     : PyCharm
# @time    : 2021/4/26 21:48
from mySettings import url, username, password
from selenium import webdriver


class Driver:
    # 初始化为空
    driver = None

    @classmethod
    def get_driver(cls, browser_name="chrome"):
        """
        获取浏览器驱动对象
        第一次调用，则生成并返回
        第二次及以后调用，则直接返回
        :return:
        """
        if cls.driver is None:
            if browser_name == "chrome":
                cls.driver = webdriver.Chrome()
            elif browser_name == "firefox":
                cls.driver = webdriver.Firefox()

            # 隐式等待
            cls.driver.implicitly_wait(5)
            # 最大化窗口
            cls.driver.maximize_window()
            # 访问到项目的网址
            cls.driver.get(url)
            # 登录用户
            cls.login()

        return cls.driver

    @classmethod
    def login(cls):
        """登录用户"""
        cls.driver.find_element_by_id("username").send_keys(username)
        cls.driver.find_element_by_id("password").send_keys(password)
        cls.driver.find_element_by_id("btnLogin").click()


if __name__ == '__main__':
    a1 = Driver().get_driver()
    a2 = Driver().get_driver()
    a3 = Driver().get_driver()
