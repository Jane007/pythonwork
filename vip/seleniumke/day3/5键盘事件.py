# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 5键盘事件.py
# @ide     : PyCharm
# @time    : 2021/4/25 22:01

from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://127.0.0.1:8088/")

# 找到用户名输入框，并输入用户名
driver.find_element_by_name("username").send_keys("libai")
driver.find_element_by_name("username").send_keys(Keys.CONTROL, "a")

Keys.BACK_SPACE  # 删除键
Keys.ENTER # 回车键
Keys.SPACE # 空格键