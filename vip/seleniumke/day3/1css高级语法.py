# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 1css高级语法.py
# @ide     : PyCharm
# @time    : 2021/4/25 20:18

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("file:///D:/Users/lenovo/PycharmProjects/script/study/seleniumStu/day3/css%E9%AB%98%E7%BA%A7%E8%AF%AD%E6%B3%95%E5%AD%A6%E4%B9%A0.html")

ret = driver.find_element_by_css_selector(".l132").text
print(ret)
