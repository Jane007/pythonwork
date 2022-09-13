# @Project : pythonwork
# @File    : lianxi.py
# @Author  : zhangjing
# @Time    : 2022/8/16 16:55
# @Software : Pycharm
# @Description :

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.action_chains import ActionChains

import time
# 创建浏览器对象
s = Service('../chromedriver.exe')
driver = webdriver.Chrome(service=s)
url = 'http://zeno-manager.xwkj.local/#/passport/login?sessionId=e168889d-264a-4a18-a08e-eb56e86965c5'
driver.maximize_window()
driver.get(url=url)
#name="ion-input-0"
driver.find_element(by=by.By.XPATH,value='//input[@class="ng-untouched ng-pristine ng-invalid ant-input ant-input-lg"]').send_keys('15010224947')
obj = driver.find_element(by=by.By.XPATH,value='//input[@type="password"]').send_keys("123456")
#v = obj.get_attribute('placeholder')
driver.find_element(by=by.By.XPATH,value="//button").click()
time.sleep(2)


#截全屏
# driver.get_screenshot_as_file('./a.png')
#
# # synacic-all  根据css样式截部分
# eli = driver.find_element(by=by.By.CSS_SELECTOR,value='.synacic-all')
# eli.screenshot('./b.png')


#鼠标操作
#class = yuanquan
driver.maximize_window()
time.sleep(2)
#ng-star-inserted
#eli = driver.find_element(by=by.By.XPATH,value='//p[@name="cut_str"]')
eli = driver.find_element(by=by.By.CLASS_NAME,value='arrows')

#ActionChains(driver).move_to_element(eli).perform()

#鼠标单击click,双击 double_click，右击context_click，拖拽drag_and_drop(ele1, ele2)
ActionChains(driver).click(eli).perform()