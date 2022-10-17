# -*- coding:utf-8 -*-


from appium import webdriver

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
    "unicodeKeyboard": True,
    "resetKeyboard": True
    # 'skipServerInstallation':True#跳过UI2的安装，如果第一次运行程序，不要添加该配置
}
# 启动session--参数：appium服务端地址，配置项
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 隐式等待
driver.implicitly_wait(10)

# 点击 boss 直聘上的放大镜  # 在 appium自动化中，元素定位以class属性代替标签名
driver.find_element("xpath",
    "//*[@resource-id='com.hpbr.bosszhipin:id/ly_menu']/android.widget.RelativeLayout[2]").click()
# 对输入框输入值--软件测试，被输入值的元素一定是 EditText
driver.find_element("id","com.hpbr.bosszhipin:id/et_search").send_keys("软件测试")
# 选择第一个搜索结果
driver.find_element("xpath","//*[@resource-id='com.hpbr.bosszhipin:id/lv_matcher']/*[1]").click()
