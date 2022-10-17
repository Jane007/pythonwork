# @Project : pythonwork
# @File    : mystartapp.py
# @Author  : zhangjing
# @Time    : 2022/9/13 10:06
# @Software : Pycharm
# @Description :
# -*- coding:utf-8 -*-

from appium import webdriver

# 设备的连接信息
from appium.webdriver.common.appiumby import AppiumBy

from vip.app.day1.settings import jingdong_desired_caps

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",jingdong_desired_caps)
driver.implicitly_wait(10)

#driver.find_element("xpath","//android.widget.ImageView[@resource-id='com.taobao.idlefish:id/iv_all_category']").click()
#driver.find_element("xpath","//android.widget.TextView[@text='生活百货' and @content-desc='生活百货']").click()

#driver.find_element(AppiumBy.ACCESSIBILITY_ID,'天猫超市').click()

#driver.find_element(AppiumBy.ID,'com.taobao.taobao:id/sv_search_view"]').click()

#driver.find_element(AppiumBy.ACCESSIBILITY_ID,'搜索').click()