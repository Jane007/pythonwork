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

# 点击右上角加号
driver.find_element_by_xpath("//*[@resource-id='com.hpbr.bosszhipin:id/ly_menu']/*[1]").click()
# 点击【继续添加求职期望】
driver.find_element_by_id("com.hpbr.bosszhipin:id/mAddJobIntent").click()
# 点击期望职位
driver.find_element_by_id("com.hpbr.bosszhipin:id/iv_position").click()
# 输入期望职位
driver.find_element_by_id("com.hpbr.bosszhipin:id/et_search").send_keys("糕点")
# 点击搜索出来的第一个
driver.find_element_by_xpath("//*[@resource-id='com.hpbr.bosszhipin:id/lv_search0']/*[1]").click()
# 点击期望薪资
driver.find_element_by_id("com.hpbr.bosszhipin:id/iv_salary").click()
# 直接点击确定按钮，使用默认值
driver.find_element_by_id("com.hpbr.bosszhipin:id/tv_confirm").click()
