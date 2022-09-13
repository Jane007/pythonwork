# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
"""
selenium 是一个网页自动化测试工具，使用它可以操作浏览器模仿人的行为
"""

# 1 元素定位  单个节点定位 find_element_by_xxx
driver.find_element_by_id()
driver.find_element_by_class_name()
driver.find_element_by_name()
driver.find_element_by_tag_name()
driver.find_element_by_css_selector()
driver.find_element_by_xpath()
driver.find_element_by_link_text()
driver.find_element_by_partial_link_text()
# 用这种方式定位，如果页面上有多个符合条件的元素，只会返回第一个
# 若页面上匹配不到我需要的元素，则会返回 NoSuchElement 的异常
driver.find_element(By.NAME, "dasd")
# 2 元素定位，匹配多个节点 find_elements_by_xxx
driver.find_elements_by_id()
driver.find_elements_by_class_name()
driver.find_elements_by_name()
driver.find_elements_by_tag_name()
driver.find_elements_by_css_selector()
driver.find_elements_by_xpath()
driver.find_elements_by_link_text()
driver.find_elements_by_partial_link_text()
# 以此种方式定位，会返回一个列表，将页面上找到的元素都依次存入这个列表
# 如果一个也找不到，则会返回空列表--基于此特性，可以用来判断元素是否存在
driver.find_elements(By.NAME, "dasd")

# css 和 xpath
#   在 web ui自动化测试当中，css用的最多
#   在 APP ui自动化测试当中，xpath用的最多

# 推荐定位的优先级
#   优先级最高：id
#   优先级其次：name
#   优先级再次：css
#   优先级最次：xpath
#   至于  class_name tag_name  link_text  partial_link_text 几乎不用
# 一般不适用JavaScript定位、操作元素，除非页面限制，我们无法用selenium操作，这时候，可以选用JavaScript
"""
关于 css 和 xpath 的优先级
    项目中，我们用的最多的就是css和xpath，关于这两个，我们优先选择 css
        1、css是配合HTML工作的，是一种匹配模式定位
           而 xpath 是配合 xml 工作的，通过遍历定位的
           所以两者在设计上，css 的性能更优秀
        2、css 的语法更简洁
        3、前端开发主要用的就是 css，不使用 xpath，所以在技术层面上，使用css可以获得更多的帮助
    
    但也不能一棒子把xpath打死，xpath也有其优点
        1、xpath 可以通过元素文本定位，而 css 不可以
        2、xpath 可以通过子节点来定位元素，而 css 不可以
        3、xpath 可以用来测试所有的安卓应用，但 css 只能在混合应用的 webview部分使用
"""

# 3 元素的操作  手工测试，是用眼睛找到元素然后操作，自动化使用代码找到元素，然后操作
ele = driver.find_element_by_id("kw")
ele.click()  # 点击元素
ele.text  # 获取元素的文本值
ele.send_keys()  # 如果元素是个文本框，我们还可以去输入内容
ele.clear()  # 清除文本框的内容
ele.get_attribute()  # 获取元素的属性值
ele.size  # 获取元素的尺寸

# 元素等待
"""
大多数web应用，都是 Ajax 和JavaScript开发的。
就容易出现元素未加载而代码已经定位到的现象，此时就会抛出异常，元素找不到

webdriver 提供了两种类型的等待，显示等待和隐式等待
    隐式等待：设置一个超时时间，在这个时间内不断的寻找元素，超时找不到就会抛出异常
    显示等待：设置一个超时时间和元素查找条件，在这个时间内不断的寻找元素，超时找不到就会抛出异常
"""

# 控制浏览器操作
driver.set_window_size(600, 600)
driver.minimize_window()
driver.maximize_window()  # 最常用，最大化浏览器
driver.back()
driver.refresh()
driver.forward()

# 窗口截图，在测试用例里边，一些重要的操作步骤，可以截图保存在测试报告里边
driver.get_screenshot_as_file("./a.png")
ele.screenshot("./a.png")

# 警告框处理
al = driver.switch_to.alert
al.dismiss()
al.accept()
al.send_keys()
al.text

# 鼠标事件
"""
用selenium 做自动化，有时候遇到模拟鼠标才能操作的情况，比如单击、双击、鼠标悬停
selenium 给我们提供了 ActionsChains 类处理这些问题
"""
from selenium.webdriver.common.action_chains import ActionChains

ActionChains(driver).click(ele).perform()
ActionChains(driver).double_click(ele).perform()
ActionChains(driver).context_click(ele).perform()
ActionChains(driver).move_to_element(ele).perform()
ActionChains(driver).drag_and_drop(ele, ele).perform()
# 支持链式调用
ActionChains(driver).move_to_element(ele).click().move_to_element(ele).perform()

# 键盘事件
"""
Keys 类几乎提供了键盘上所有的按键方法
"""
from selenium.webdriver.common.keys import Keys

# 只要能联想出来，就证明提供了
Keys.UP
Keys.DOWN
ele.send_keys(Keys.CONTROL, "a")

# 文件上传
"""
对于 input 标签实现的文件上传功能，可以将其看做是一个输入框，直接 send_keys 指定本地
文件路径就可以实现文件上传。

对于非 input 标签实现的文件上传功能，可以通过模拟键盘敲击的方式实现
"""

# 内嵌网页
"""
iframe, 又叫浮动标记帧，可以把一个html镶嵌在另一个HTML里边
"""
driver.switch_to.frame(ele)
driver.switch_to.default_content()
driver.switch_to_frame()  # 将来会被删除的方法，不建议使用

# 多标签页
driver.current_window_handle  # 获取当前标签页句柄
driver.window_handles  # 获取所有标签页的句柄
driver.switch_to.window()  # 切换到对应的标签页
driver.close()  # 关闭当前标签页

# 页面滚动 # 通过 JavaScript 实现
driver.execute_script()

# po 模式
"""
po 模式是一种设计思想，应用在selenium自动化上

在传统设计模式中，新增测试用例之后，代码会有以下几个问题
    1、易读性差：一连串的 find_element 会使代码杂乱无章
    2、复用性差：没有公共方法，很难复用
    3、可维护性差：一但元素发生变化，需要维护、修改大量的测试用例
    
因此考虑到优化：
    po模式是一种自动化设计模式，将页面定位和业务操作分开来，
    也就是把元素的定位和测试脚本分开，从而提供可维护性

首先封装一个 basePage 类，这个基类拥有一些webdriver实例的属性，
然后每一个 page 继承 basePage，可以通过 driver 管理每一个 page 中的元素
而且 page 中将一些常用的元素操作封装成方法
testCase 依赖 page，进行测试用例步骤的组织
"""

# appium 测试范围
"""
原生应用
混合 
web应用

对电脑端网页测试--用selenium，操作执行在电脑上的浏览器
对手机端玩个测试--
                用 selenium 也可以，操作执行者电脑上浏览器的开发者模式
                用 appium 也可以，操作执行在手机上的浏览器
混合应用--用 appium，操作执行在手机 APP 里边
"""
from appium import webdriver

desired_caps = {}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# appium 的元素定位
"""
appium 
    id、class、AccessibilityId、xpath、AndroidUIAutomator
    对于手机 h5 页面，也支持 selenium 中的定位方式
selenium
    id， class, name, tag name, link text, paratial link text, xpath, css
"""

# appium 的操作
ele = driver.find_element_by_id()

ele.click()
ele.clear()
ele.send_keys()
ele.text
ele.size
ele.location  # 获得元素的位置

# 手机触摸操作
driver.swipe()  # 滑动
# 单点触摸
from appium.webdriver.common.touch_action import TouchAction
    # 多点触摸
from appium.webdriver.common.multi_action import MultiAction

# 手机操作
driver.get_window_size()
driver.get_screenshot_as_file()
driver.network_connection
driver.set_network_connection()
