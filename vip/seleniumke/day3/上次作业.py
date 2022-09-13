# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 上次作业.py
# @ide     : PyCharm
# @time    : 2021/4/25 22:05

from selenium.webdriver.support.ui import Select
from selenium import webdriver
import datetime

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://127.0.0.1:8088/")

# 找到用户名输入框，并输入用户名
driver.find_element_by_name("username").send_keys("libai")
# 找到密码输入框，并输入密码
driver.find_element_by_name("password").send_keys("opmsopms123")
# 找到登录按钮，并点击
driver.find_element_by_tag_name("button").click()

# 点击审批管理
driver.find_element_by_css_selector(
    "[class=\"nav nav-pills nav-stacked custom-nav js-left-nav\"] > li:nth-child(4)").click()
# 点击请假
driver.find_element_by_css_selector("[class=\"jumbotron text-center\"] > span > a:nth-child(1)").click()
# 点击我要请假
driver.find_element_by_css_selector("[class=\"btn btn-success\"]").click()
# 请假类型选事假
Select(driver.find_element_by_name("type")).select_by_index(1)

# 计算请假开始时间
# 获取当前时间
now = datetime.datetime.now()
# 计算时间增量
dalta = datetime.timedelta(days=1)
# 开始时间
st = (now + dalta).strftime("%Y-%m-%d")
# 计算时间增量
dalta = datetime.timedelta(days=3)
# 结束时间
ed = (now + dalta).strftime("%Y-%m-%d")

# 输入请假开始时间，开始时间写 明天
driver.find_element_by_name("started").send_keys(st)
# 输入结束时间
driver.find_element_by_name("ended").send_keys(ed)

# 输入请假天数
driver.find_element_by_name("days").clear()
driver.find_element_by_name("days").send_keys("3")
# 输入请假事由
driver.find_element_by_name("reason").send_keys("请假事由")
# 选择审批人
driver.find_element_by_css_selector(".addAvatar").click()
# 选择第一个人作为审批人
driver.find_element_by_css_selector(".list-unstyled > :nth-child(1)").click()
# 点击提交
driver.find_element_by_css_selector("[class=\"btn btn-primary\"]").click()
