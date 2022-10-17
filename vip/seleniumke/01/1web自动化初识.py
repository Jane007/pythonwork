# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 1web自动化初识.py
# @ide     : PyCharm
# @time    : 2021/4/21 20:23

"""
1、测试脚本，也就是你我写的代码，可以是python也可以是java，也可以被叫做 client 端
2、浏览器驱动，是根据不同浏览器开发的
3、浏览器

脚本操作驱动，驱动操作浏览器，浏览器将结果返回给驱动，驱动返回给脚本



HTML，也可以叫做页面标签，也会叫做元素

HTML以开始标签起始，以结束标签终止，但有一些例外
    部分HTML元素具有空内容
    以开始标签的结束而结束
元素的内容是开始标签与结束标签之间的内容
大多数HTML元素有属性
    属性一般描述于开始标签
    属性相当于给标签添加了描述信息
    属性通常以键值对形式出现
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by

# 创建浏览器对象
s = Service('../chromedriver.exe')
driver = webdriver.Chrome(service=s)
url = 'https://www.baidu.com'
# 请求百度
#driver.set_window_size(100,300)
driver.get(url=url)

# 找到看过框
driver.find_element(by=by.By.NAME,value='wd').send_keys('python')
# 找到登录按钮，并点击
driver.find_element(by=by.By.ID,value='su').click()



