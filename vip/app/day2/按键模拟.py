# -*- coding:utf-8 -*-

from appium import webdriver
from settings import desired_caps
import time

# 启动session--参数：appium服务端地址，配置项
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 隐式等待
driver.implicitly_wait(10)

# 音量增加
driver.keyevent(24)
time.sleep(3)
# 音量减少
driver.keyevent(25)

# 拨号键 5
# 挂机键 6
# 返回键 4
# 电源键 26
