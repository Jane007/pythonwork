# -*- coding:utf-8 -*-

# 准备自动化配置信息
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

x = {
    "platformName": "Android",
    "plathformVersion": "10",
    "deviceName": "X4UOCQOF79AUZX79",
    "appPackage": "com.hpbr.bosszhipin",
    "appActivity": ".module.launcher.WelcomeActivity",
    "noReset": "True",
    "newCommandTimeout": 6000,
    "automationName": "UiAutomator2"
}
