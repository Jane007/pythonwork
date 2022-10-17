# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 2iframe.py
# @ide     : PyCharm
# @time    : 2021/4/26 20:35

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://127.0.0.1:8088/album/upload")

# 找到用户名输入框，并输入用户名
driver.find_element_by_name("username").send_keys("libai")
# 找到密码输入框，并输入密码
driver.find_element_by_name("password").send_keys("opmsopms123")
# 找到登录按钮，并点击
driver.find_element_by_tag_name("button").click()

driver.find_element_by_css_selector(
    "body > section > div.left-side.sticky-left-side > div.left-side-inner > ul > li:nth-child(2) > a").click()
driver.get("http://127.0.0.1:8088/project/add")

# 找到内嵌网页
ele = driver.find_element_by_css_selector("[class=\"ke-edit-iframe\"]")
# 进入内嵌网页
driver.switch_to.frame(ele)
# 进入内嵌网页后就可以操作内嵌网页中的元素了
driver.find_element_by_css_selector(".ke-content").send_keys("123\nabc")

# 进入内嵌网页以后，操作内嵌网页外的元素，是操作不到的
# 离开内嵌网页，切换回主页面
driver.switch_to.default_content()
driver.find_element_by_name("name").send_keys("123")