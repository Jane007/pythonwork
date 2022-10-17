# -*- coding:utf-8 -*-


from appium import webdriver

caps = {
    "platformName": "Android",
    "plathformVersion": "10",
    "deviceName": "X4UOCQOF79AUZX79",
    "browserName": "Chrome",
    # 要在电脑上装一个与手机里边的浏览器版本相对应的驱动
    # 要注意一下，名字重命名，防止和电脑上的浏览器驱动冲突
    # 驱动的安装方式和selenium是一样的
    "chromedriverExecutable": "D:/tool/selenium/python/chromedriver_81.exe",
    "noReset": "True",
    "newCommandTimeout": 6000,
    "automationName": "UiAutomator2"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

driver.get("http://120.55.190.222:38080/#/")


driver.find_element_by_css_selector(".uni-input-input").click()
driver.find_element_by_css_selector(".uni-input-input").send_keys("123456")