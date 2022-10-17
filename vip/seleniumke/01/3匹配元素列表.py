# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 3匹配元素列表.py
# @ide     : PyCharm
# @time    : 2021/4/21 22:02
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8088/login")

# driver.find_element_by_class_name("form-control").send_keys("123")
"""
find_element，会返回找到的第一个元素，如果根据表达式找不到元素，就报错
find_elements，会寻找页面上所有满足表达式的元素，将所有能找到的元素存在一个列表里，如果一个找不到，那就返回空列表
"""

# 寻找所有class属性为 form-control 的元素，存入列表，列表赋值给变量 eleSli
eleSli = driver.find_elements_by_class_name("form-control")

# 声明了一个列表
txtSli = ["111", "222"]

# 事先知道 eleSli 列表中有两个元素，所以设置循环为两次
for idx in range(2):

    # eleSli[idx] 每次循环，根据下标取出 eleSli中的内容 -- 一个元素
    # 对这个元素输入文本，文本内容来源于 txtSli，取相同的下标
    eleSli[idx].send_keys(txtSli[idx])
