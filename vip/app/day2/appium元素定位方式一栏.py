# -*- coding:utf-8 -*-

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from settings import desired_caps


# 启动session--参数：appium服务端地址，配置项
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 隐式等待
driver.implicitly_wait(10)

# 通过 id 定位
driver.find_element("id","元素的resource-id值")

# 根据 class name 进行定位, 很少用，因为大部分时候都不唯一
driver.find_element("name","android.widget.ImageView")

# 根据 AccessibilityId 定位，取得是元素的 content_desc
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID.XPATH,value="ddadasfs")

# xpath 定位
# APP里边的 xpath 和我们之前学的 selenium 一样
# 只不过用 class name 取代 tag name

# 根据文本定位--一般不推荐使用，因为不精准
driver.find_element("xpath","//*[text()='golang开发工程师']")
# 文本定位  模糊定位
driver.find_element("xpath","//*[contains(@text, '开发')]")
# 下标定位
driver.find_element("xpath","//*[@resource-id='com.hpbr.bosszhipin:id/lv_matcher']/*[1]").click()
# 组合定位
driver.find_element("xpath","//*[@class='xxx' and text()='aaa']")
driver.find_element("xpath","//*[@class='xxx' and contains(@text, '开发')")

# 以上是 appium 提供的定位方式
# 还可以通过 Android UIAutomator
# 根据文本定位--精确文本
driver.find_element("-android uiautomator","newUiSelector().text('文本内容')")
# 根据文本定位--模糊文本
driver.find_element("-android uiautomator","newUiSelector().textContains('可以使用模糊文本')")
# 文本以xxx开始
driver.find_element("-android uiautomator","newUiSelector().textStartWith('xxx')")
# 正则表达式匹配文本
driver.find_element("-android uiautomator","newUiSelector().textMatches('.*+')")
# 根据id定位
driver.find_element("-android uiautomator","newUiSelector().resourceId('xxx')")
# 根据id定位, 但是支持正则匹配
driver.find_element("-android uiautomator","newUiSelector().resourceIdMatches('^abc.+')")
# 根据 class name定位
driver.find_element("-android uiautomator","newUiSelector().className('sdfsf')")
# 根据 class name定位, 但是支持正则匹配
driver.find_element("-android uiautomator","newUiSelector().classNameMatches('^abc.+')")
# 将多个条件组合起来，以链式调用的方式，以下匹配 id为xxx且文本为我的
driver.find_element("-android uiautomator","newUiSelector().resourceId('xxx').text('我的')")
# 支持父子定位，以下等同于 //*[@resource-id='com.hpbr.bosszhipin:id/lv_matcher']/*[text()='我的']
driver.find_element("-android uiautomator","newUiSelector().resourceIdMatches('^abc.+').childSelector(text('我的'))")


"""
selenium 
    id，class name，name，tag name，link text，xpath，css
appium
    id，classname，xpath，AccessibilityId，android_uiautomator
"""


# 关于元素操作，appium和selenium是一样的
driver.find_element("xpath","//*[text()='golang开发工程师']").click()
driver.find_element("xpath","//*[text()='golang开发工程师']").send_keys("dsad")
driver.find_element("xpath","//*[text()='golang开发工程师']").clear()
txt = driver.find_element("xpath","//*[text()='golang开发工程师']").text
