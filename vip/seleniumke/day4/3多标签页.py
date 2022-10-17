# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 3多标签页.py
# @ide     : PyCharm
# @time    : 2021/4/26 21:03
from selenium import webdriver

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

# 点击 opms 官网
driver.find_element_by_link_text("OPMS官网").click()

# 获取到所有的窗口
handle_sli = driver.window_handles
# 循环所有的窗口
for handle in handle_sli:
    # 切换到当次循环的窗口
    driver.switch_to.window(handle)
    # if driver.title == "OPMS-项目管理软件+OA管理软件+CRM管理软件":
    #     break
    if driver.find_elements_by_css_selector("[class=\"container marketing\"] > div:nth-child(2) h2"):
        break

# 获取新标签页上的某个元素的文本
txt = driver.find_element_by_css_selector("[class=\"container marketing\"] > div:nth-child(2) h2").text
print(txt)


