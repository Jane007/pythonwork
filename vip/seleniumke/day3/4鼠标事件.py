# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 4鼠标事件.py
# @ide     : PyCharm
# @time    : 2021/4/25 21:54

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://127.0.0.1:8088/")

# 找到用户名输入框，并输入用户名
driver.find_element_by_name("username").send_keys("libai")
# 找到密码输入框，并输入密码
driver.find_element_by_name("password").send_keys("opmsopms123")
# 找到登录按钮，并点击
driver.find_element_by_tag_name("button").click()

ele = driver.find_element_by_css_selector("[class=\"btn btn-default dropdown-toggle\"]")
# 鼠标悬停
ActionChains(driver).move_to_element(ele).perform()
# 单击（有时候，一些无法click的，可以用鼠标事件点击
ActionChains(driver).click(ele).perform()
# 双击
ActionChains(driver).double_click(ele).perform()
# 右击
ActionChains(driver).context_click(ele).perform()
# 拖拽
ActionChains(driver).drag_and_drop(ele1, ele2).perform()

