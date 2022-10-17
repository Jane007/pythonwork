# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 1文件上传.py
# @ide     : PyCharm
# @time    : 2021/4/26 20:04

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import win32com
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://127.0.0.1:8088/album/upload")

# 找到用户名输入框，并输入用户名
driver.find_element_by_name("username").send_keys("libai")
# 找到密码输入框，并输入密码
driver.find_element_by_name("password").send_keys("opmsopms123")
# 找到登录按钮，并点击
driver.find_element_by_tag_name("button").click()

# 只是找元素，不做任何操作，更加高效的判断登录加载是否完成
driver.find_elements_by_link_text("开启OPMS之旅")

driver.get("http://127.0.0.1:8088/album/upload")

# # 对于 input 标签实现的文件上传，可以将其视为一个输入框
# # 直接send_keys 文件路径即可
# driver.find_element_by_id("albumUpload").send_keys("D:\desktop\QQ截图20210426200232.png")

# 如果是非 input 标签，则通过模拟按键操作的形式进行文件上传
ActionChains(driver).click(driver.find_element_by_id("albumUpload")).perform()
time.sleep(3)
# 模拟键盘敲击，1-按键需要保持英文输入法状态  2-文件路径不能有中文  3-代码执行时，自己不能动键盘
sh = win32com.client.Dispatch("WScript.shell")
sh.Sendkeys("D:\desktop\\abb.png")
