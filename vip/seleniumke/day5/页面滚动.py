# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 页面滚动.py
# @ide     : PyCharm
# @time    : 2021/4/28 20:04

from selenium import webdriver
import time

# 创建浏览器对象
driver = webdriver.Chrome()
driver.implicitly_wait(5)
# 访问到宝利商城的网址
driver.get("http://127.0.0.1:8088/login")

# 找到用户名输入框，并输入用户名
driver.find_element_by_name("username").send_keys("libai")
# 找到密码输入框，并输入密码
driver.find_element_by_name("password").send_keys("opmsopms123")
# 找到登录按钮，并点击
driver.find_element_by_tag_name("button").click()

time.sleep(1)
driver.get("http://127.0.0.1:8088/album/66621262012616704")

# driver.execute_script("window.scrollBy(0, 500)")
# 向下滚动500个像素点 window.scrollBy(0, 500)
# 向上滚动500个像素点 window.scrollBy(0, -500)
# 向左滚动500个像素点 window.scrollBy(-500, 0)
# 向右滚动500个像素点 window.scrollBy(500, 0)

# 滚动至指定的元素可见
ele = driver.find_element_by_css_selector(".activity-list > li:nth-child(6) p")
driver.execute_script("arguments[0].scrollIntoView()", ele)

# 如果是元素内自带的滚动条
js = 'document.querySelector(".scroll").scrollTop = 100'
driver.execute_script(js)
# 左右滚动
js = 'document.querySelector(".scroll").scrollLeft = 100'
