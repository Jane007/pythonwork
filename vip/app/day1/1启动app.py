# -*- coding:utf-8 -*-

from appium import webdriver

# 设备的连接信息
desired_caps = {
    # 被测平台
    "platformName": "Android",
    # 系统版本号，保留到整数位即可
    "platformVersion": "10",
    # 设备名，通过 adb devices 获取
    "devicesName": "X4UOCQOF79AUZX79",
    # 应用程序包名, 建议向移动端开发获取
    "appPackage": "com.taobao.idlefish",
    # Activity 类名
    "appActivity": "com.taobao.fleamarket.home.activity.MainActivity",
    # 设置自动化后不重置app
    "noReset": True,
    # 设置一个超时时间, 单位是秒
    "newCommandTimeout": 60,
    # 设置底层驱动
    "automationName": "UiAutomator2"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)

driver.find_element("xpath","//android.widget.ImageView[@resource-id='com.taobao.idlefish:id/iv_all_category']").click()
driver.find_element("xpath","//android.widget.TextView[@text='生活百货' and @content-desc='生活百货']").click()

