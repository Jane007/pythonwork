# -*- coding:utf-8 -*-

from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "X4UOCQOF79AUZX79",
    "appPackage": "com.example.haiwen.myhybirdapp",
    "appActivity": ".MainActivity",
    "noReset": "True",
    "newCommandTimeout": 6000,
    "automationName": "UiAutomator2"
}

# 启动混合应用
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)

# 控制原生的控件
driver.find_element_by_id("com.example.haiwen.myhybirdapp:id/editText").send_keys("https://www.baidu.com")
driver.find_element_by_id("com.example.haiwen.myhybirdapp:id/button").click()

# 查看当前手机上 APP的 contexts
print(driver.contexts)
# 切换到 webview contexts
driver.switch_to.context("WEBVIEW_com.example.haiwen.myhybirdapp")


# 当我们在操作 webview的部分，是可以使用一切selenium的定位语法的
# # 操作webview部分
driver.find_element_by_id("kw").send_keys("123456")
