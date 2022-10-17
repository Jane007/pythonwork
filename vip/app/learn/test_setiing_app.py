# @Project : pythonwork
# @File    : test_setiing_app.py
# @Author  : zhangjing
# @Time    : 2022/9/21 11:15
# @Software : Pycharm
# @Description :
from appium import webdriver

# 设备的连接信息
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains

desired_caps = {
    # 被测平台
    "platformName": "Android",
    # 系统版本号，保留到整数位即可
    "platformVersion": "8",
    # 设备名，通过 adb devices 获取
    "devicesName": "X4UOCQOF79AUZX79",
    # 应用程序包名, 建议向移动端开发获取
    "appPackage": "com.android.settings",
    # Activity 类名
    "appActivity": ".MonitoringCertInfoActivity",
    # 设置自动化后不重置app
    "noReset": True,
    # 设置一个超时时间, 单位是秒
    "newCommandTimeout": 60,
    # 设置底层驱动
    "automationName": "UiAutomator2"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("锁屏、密码和指纹")').click()

myAction = ActionChains(driver)
myAction.w3c_actions.pointer_action.move_to_location(500,1200)
myAction.w3c_actions.pointer_action.pointer_down()


myAction.w3c_actions.pointer_action.move_to_location(600,1400)
myAction.w3c_actions.pointer_action.pointer_down()

myAction.w3c_actions.pointer_action.release()
myAction.perform()
