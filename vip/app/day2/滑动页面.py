# -*- coding:utf-8 -*-


from appium import webdriver
from settings import desired_caps

# 启动session--参数：appium服务端地址，配置项
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 隐式等待
driver.implicitly_wait(10)

# [414,895][630,928]
driver.swipe(100, 100, 200, 200, 10)

# # 从一个元素滑动到另一个元素，没有惯性
# driver.drag_and_drop(ele1, ele2)
#
# # 从一个元素滑动到另一个元素，有惯性
# driver.scroll(ele1, ele2)
