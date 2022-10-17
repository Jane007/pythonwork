# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 5上次作业.py
# @ide     : PyCharm
# @time    : 2021/4/23 21:55
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://127.0.0.1:8088/")

# 找到用户名输入框，并输入用户名
driver.find_element_by_name("username").send_keys("libai")
# 找到密码输入框，并输入密码
driver.find_element_by_name("password").send_keys("opmsopms123")
# 找到登录按钮，并点击
driver.find_element_by_tag_name("button").click()

# 点击员工相册
driver.find_element_by_xpath("//i[@class='fa fa-plane']").click()
time.sleep(0.3)
# 点击油菜花
driver.find_element_by_xpath("//*[@id='gallery']/div[1]/p/a").click()
# 向下滑动 900 个像素点
driver.execute_script("window.scrollBy(0, 900)")
# 输入一条评论
driver.find_element_by_name("comment").send_keys("输入一条评论")
# 点击提交评论
driver.find_element_by_xpath("//button[@class='btn btn-primary pull-right']").click()
