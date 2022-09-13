# -*- coding:utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://120.55.190.222:38080/#/")

# 点击我的按钮
driver.find_element_by_css_selector("body > uni-app > uni-tabbar > div.uni-tabbar > div:nth-child(6)").click()

driver.execute_script("window.scrollBy(0, 500)")