# -*- coding:utf-8 -*-

from selenium import webdriver

# 以开发者模式打开
options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})
driver = webdriver.Chrome(options=options)


driver.implicitly_wait(5)
driver.get("http://120.55.190.222:38080/#/pages/index/user")

driver.execute_script("window.scrollBy(0, 500)")
