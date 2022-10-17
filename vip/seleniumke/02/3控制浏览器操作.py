# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 3控制浏览器操作.py
# @ide     : PyCharm
# @time    : 2021/4/23 20:58
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://www.baidu.com")

# 参数数字为像素点, 设置高和宽
driver.set_window_size(600, 600)
time.sleep(3)

# 最大化浏览器
driver.maximize_window()
time.sleep(3)

# 最小化浏览器
driver.minimize_window()
time.sleep(3)

