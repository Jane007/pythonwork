# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 2webdriver常用方法.py
# @ide     : PyCharm
# @time    : 2021/4/23 20:48
"""
click  单击元素
send_keys  对文本框输入内容
clear  清除文本框的内容
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# 创建浏览器对象
s = Service('../chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(5)
driver.get("http://127.0.0.1:8088/")

# 找到用户名输入框，并输入用户名
driver.find_element_by_name("username").send_keys("libai")
# 找到密码输入框，并输入密码
driver.find_element_by_name("password").send_keys("opmsopms123")
# 找到登录按钮，并点击
driver.find_element_by_tag_name("button").click()

# 获取页面的标题
print(driver.title)
# 获取页面的 url
print(driver.current_url)
# 获取标签对之间的文本信息----常用
ele = driver.find_element_by_css_selector(
    "body > section > div.left-side.sticky-left-side > div.left-side-inner > ul > li:nth-child(1) > a > span")
print(ele.text)
