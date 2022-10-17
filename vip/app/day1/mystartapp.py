# @Project : pythonwork
# @File    : mystartapp.py
# @Author  : zhangjing
# @Time    : 2022/9/13 10:06
# @Software : Pycharm
# @Description :
# -*- coding:utf-8 -*-
import time

from appium import webdriver

# 设备的连接信息
from appium.webdriver.common.appiumby import AppiumBy

from vip.app.day1.settings import taobao_desired_caps

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",taobao_desired_caps)
driver.implicitly_wait(10)

#driver.find_element("xpath","//android.widget.ImageView[@resource-id='com.taobao.idlefish:id/iv_all_category']").click()
#driver.find_element("xpath","//android.widget.TextView[@text='生活百货' and @content-desc='生活百货']").click()

#driver.find_element(AppiumBy.ACCESSIBILITY_ID,'天猫超市').click()

ele = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"水龙头过滤")
if ele is not None:
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,'搜索').click()
else :
    print("没发现元素")
time.sleep(2)
driver.quit()
#driver.find_element("-android uiautomator","newUiSelector().resourceId('com.taobao.taobao:id/searchEdit').text('儿童水杯')")

# driver.find_element(AppiumBy.XPATH,'com.taobao.taobao:id/search_bar_wrapper"]').send_keys("儿童水杯")
# time.sleep(2)
#driver.find_element(AppiumBy.ID,'com.taobao.taobao:id/searchbtn').click()
