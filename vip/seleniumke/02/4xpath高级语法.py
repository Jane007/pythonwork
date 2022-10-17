# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 3xpath高级语法.py
# @ide     : PyCharm
# @time    : 2021/4/23 21:15
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://127.0.0.1:8088/login")

"""
xpath 使用路径表达式来选取 xml 或 html 中的节点或节点集
其标准语法如下：
//tagname[@attribute='value']
    //  选取后代节点
    tagname 节点标签名
    attribute 节点属性
    value  属性值

xpath 遍历所有元素
"""

# xpath 的绝对路径
driver.find_element_by_xpath("/html/body/div[1]/form/div[2]/input[1]").send_keys("libai")
# xpath 的相对路径
driver.find_element_by_xpath("//input[2]").send_keys("opmsopms123")
driver.find_element_by_xpath("//button").click()

# xpath  可以用 and 或 or 连接多个属性

# xpath 还可以根据元素文本进行定位 //*[text()=' 登录']

# 在 xpath的路径当中， / 匹配子元素   // 匹配后代元素

# xpath 中 一个点 . 代表当前节点，  两个点 .. 代表上层节点

# xpath 的下标是从 1 开始数的

# xpath 里边，class 复合类是可以包含空格找到的
