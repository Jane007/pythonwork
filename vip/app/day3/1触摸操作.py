# -*- coding:utf-8 -*-
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import time

desired_caps = {
    # 移动设备平台 Android / IOS
    'platformName': 'Android',
    # 平台OS--安卓版本号,写整数位即可
    'plathformVersion': '8',
    # 设备的名称
    'deviceName': 'X4UOCQOF79AUZX79',
    # 提供被测app的信息-包名，入口信息:
    'appPackage': 'com.hpbr.bosszhipin',
    'appActivity': '.module.launcher.WelcomeActivity',
    # 确保自动化之后不重置app
    'noReset': True,
    # 设置session的超时时间，单位秒，默认60s
    'newCommandTimeout': 6000,
    # 设置底层测试驱动-1.15默认使用的底层驱动就是UiAutomator2
    'automationName': 'UiAutomator2',  # 或者UiAutomator1
    # 'skipServerInstallation':True#跳过UI2的安装，如果第一次运行程序，不要添加该配置
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)

time.sleep(3)
# 按坐标点击, 持续时间可以实现长按或者短按
driver.tap([(576, 96)], 100)

ele = driver.find_element_by_id("com.hpbr.bosszhipin:id/mAddJobIntent").click()
# 短按一个元素或坐标
TouchAction(driver).press(ele).release().perform()
# TouchAction(driver).press(x=576, y=96).release().perform()

# # 长按一个元素或坐标
# TouchAction(driver).long_press(ele, duration=500).release().perform()
# TouchAction(driver).long_press(x=576, y=96, duration=500).release().perform()
#
# # 点击某个元素，多次点击
# TouchAction(driver).tap(x=122, y=143, count=3).release().perform()
# TouchAction(driver).tap(ele, count=3).release().perform()
#
# # 模拟手指等待, 比如按下某个按键五秒之后再抬起
# TouchAction(driver).press(ele).wait(5000).release().perform()
#
# # 移动，多点连线
TouchAction(driver).move_to(x=321, y=324).move_to(x=323, y=311).release().perform()
#
# # 比如想要拖动某个元素
# TouchAction(driver).press(ele).move_to(x=321, y=324).release().perform()
