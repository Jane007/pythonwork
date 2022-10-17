# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : 2ui自动化操作流程.py
# @ide     : PyCharm
# @time    : 2021/4/21 21:21

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
# 创建浏览器对象
s = Service('../chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("http://127.0.0.1:8088/login")

"""
ui 自动化主要包含两部分，一是选择界面元素，二是操作界面元素

根据元素的特征选择界面元素：
    id属性   通常是唯一的，也有不唯一的时候（随机id，重复id）
            随机id和重复id，不可以使用id进行定位
            否则，id是第一选择
    name属性 
    class
    tag_name
根据元素的关系   css、xpath

操作界面元素
    输入操作：点击、输入、拖拽
    输出操作：
"""

"""
# 定位元素的步骤
    1、找到元素对应的标签
    2、观察元素是否有可利用的属性
    3、若无法通过属性定位，则增加关系进行辅助定位
"""

# 元素定位的第一种方法，根据id定位
a = driver.find_element_by_id("login-form")

# 元素定位的第二种方法，根据 name 属性进行定位
username_input_box = driver.find_element_by_name("username")
username_input_box.send_keys("libai")

# 元素定位的第三种方法，根据class属性进行定位
#   根据 classname进行定位的时候，有时候会遇到复合类，也就是class属性中间有空格
#   class 属性比较特殊，空格代表间隔符号，表示这个元素的class属性有多个值
#   任取其中一个值就可以定位（但是不保证唯一
driver.find_element_by_class_name("xdafsdf")

# 元素定位的第四种方法, 根据标签名称进行定位
driver.find_element_by_tag_name("p")

# 元素定位的第五种方法，根据链接文本进行定位
driver.find_element_by_link_text("超链接显示在外的文本")

# 元素定位的第六种方法，根据链接文本模糊定位
driver.find_element_by_partial_link_text("超链接显示在外的文本,一部分即可，但是不能错")

# 元素定位的第七种方法，根据 css表达式进行定位
driver.find_element_by_css_selector(
    "body > section > div.left-side.sticky-left-side > div.left-side-inner > ul > li:nth-child(1) > a > span")
# 元素定位的第八种方法
driver.find_element_by_xpath("/html/body/section/div[1]/div[3]/ul/li[1]/a/i")

"""
元素定位八种方法
    1、id属性    -- 常用
    2、name属性    -- 常用
    3、class属性
    4、tag_name标签名称
    5、link_text链接文本
    6、partial_link_text链接文本模糊定位
    7、css表达式      -- 常用
    8、xpath表达式    -- 常用
"""
