# -*- coding:utf-8 -*-

from mySettings import url, username, password
from selenium import webdriver


class Driver:
    """浏览器驱动类"""
    _driver = None

    @classmethod
    def get_driver(cls, brose_name="chrome"):
        """
        获取浏览器驱动对象
        若第一次进入此函数，则创建并返回
        若第二次及以后进入此函数，则直接返回（之前已经创建好的
        :param brose_name: 浏览器驱动类型
        :return:
        """
        if cls._driver is None:
            if brose_name == "chrome":
                cls._driver = webdriver.Chrome()
            elif brose_name == "firefox":
                cls._driver = webdriver.Firefox()
            # 。。。更多的就不写了
            else:
                raise ("没有找到此类型的浏览器，请检查传入的参数", brose_name)

            cls._driver.maximize_window()
            cls._driver.implicitly_wait(5)
            cls._driver.get(url)
            cls.login()

        return cls._driver

    @classmethod
    def login(cls):
        cls._driver.find_element_by_id("username").send_keys(username)
        cls._driver.find_element_by_id("password").send_keys(password)
        cls._driver.find_element_by_id("btnLogin").click()

if __name__ == '__main__':
    Driver.get_driver()
    Driver.get_driver()
    Driver.get_driver()
