# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 1元素等待.py
# @ide     : PyCharm
# @time    : 2021/4/23 20:05

from selenium.webdriver.support import expected_conditions as ec  # 提供等待条件的
from selenium.webdriver.support.ui import WebDriverWait  # 提供等待类
from selenium.webdriver.common.by import By  # 提供元素寻找方法的
from selenium import webdriver

driver = webdriver.Chrome()
"""
隐式等待：设置一个超时时间，在这个时间内，不断的寻找元素（每隔0.5s找一次）
若超时仍未找到则抛出timeout异常，若在时间内找到了，则继续往下执行代码
优点：
    使用简单，一次添加终生有效
    一般在创建 driver 之后设置
    设置以后，在其之后执行的元素寻找都有效
缺点：
    无法指定元素进行等待
    需要等页面全部加载完成，相对而言浪费时间
"""
# driver.implicitly_wait(10)

driver.get("http://127.0.0.1:8088/")

# 找到用户名输入框，并输入用户名
driver.find_element_by_name("username").send_keys("libai")
# 找到密码输入框，并输入密码
driver.find_element_by_name("password").send_keys("opmsopms123")
# 找到登录按钮，并点击
driver.find_element_by_tag_name("button").click()

# driver.find_element_by_css_selector(
#     "body > section > div.left-side.sticky-left-side > div.left-side-inner > ul > li:nth-child(1) > a > span").click()

"""
显示等待：设置一个超时时间和一个元素查找条件，在这个时间内不断寻找元素
若超时仍未找到则抛出timeout异常，若在时间内找到了，则继续往下执行代码

优点：
    不需要等待页面全部加载完成，相对节省时间
    可以指定需要等待的元素，对于某些加载特别缓慢的元素，可以为其增加时间
缺点：
    使用相对复杂，代码多
    每次等待都需要再写一遍代码
"""


# ele = WebDriverWait(driver, 20, 0.5).until(
#     ec.visibility_of_element_located(
#         (By.CSS_SELECTOR,
#          "body > section > div.left-side.sticky-left-side > div.left-side-inner > ul > li:nth-child(1) > a > span")
#     )
# )
# ele.click()


# 可以将显示等待封装为函数
def webElementWait(driver, timeout, lo_time, by_locate, locate):
    """
    :param driver: 浏览器驱动对象
    :param timeout: 最大等待时间
    :param lo_time: 轮询时间
    :param by_locate: 元素定位方法
    :param locate: 元素定位表达式
    :return: 元素对象
    """
    return WebDriverWait(driver, timeout, lo_time).until(
        ec.visibility_of_element_located(
            (by_locate, locate)
        )
    )


ele = webElementWait(driver, 10, 0.5, By.CSS_SELECTOR,
                     "body > section > div.left-side.sticky-left-side > div.left-side-inner > ul > li:nth-child(1) > a > span")
ele.click()


"""
当隐式等待与显示等待同时出现，取时间更多的一个
比如隐式等5秒，显示等7秒，则最长等待时间为 7 秒
"""