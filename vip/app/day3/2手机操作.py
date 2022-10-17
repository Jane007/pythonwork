# -*- coding:utf-8 -*-

from appium import webdriver

desired_caps = {
    # 移动设备平台 Android / IOS
    'platformName': 'Android',
    # 平台OS--安卓版本号,写整数位即可
    'plathformVersion': '10',
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

# 读取分辨率
print(driver.get_window_size())

# 截图
driver.get_screenshot_as_file("./a.png")

# 获取手机的网络状态
# 返回的是数字
#   0 不开 WiFi 也不开数据也不开飞行模式
#   1 不开WiFi 也不开数据，但是打开飞行模式
#   2 仅 WiFi
#   4 仅数据
#   6 同时开启wifi和流量
print(driver.network_connection)

# 设置手机网络状态
driver.set_network_connection(2)

# 获取手机当前时间
print(driver.device_time)

# 打开手机任务操作栏
driver.open_notifications()
