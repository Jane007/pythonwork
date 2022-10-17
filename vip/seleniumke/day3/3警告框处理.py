# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 3警告框处理.py
# @ide     : PyCharm
# @time    : 2021/4/25 21:33

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("file:///D:/Users/lenovo/PycharmProjects/script/study/seleniumStu/day3/test.html")

# 点击对话框
driver.find_element_by_id("bu1").click()
# 获取对话框对象
al = driver.switch_to.alert
# 确认对话框
al.accept()

# 点击确认框
driver.find_element_by_id("bu2").click()
# 获取确认框对象
al = driver.switch_to.alert
# 取消确认框
al.dismiss()

# 点击提示框
driver.find_element_by_id("bu3").click()
# 获取提示框对象
al = driver.switch_to.alert
# 输入文本
al.send_keys("123")
al.accept()
