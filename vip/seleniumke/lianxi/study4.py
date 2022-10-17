# @Project : pythonwork
# @File    : study4.py
# @Author  : zhangjing
# @Time    : 2022/8/17 15:36
# @Software : Pycharm
# @Description :
import win32com.client
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
# 创建浏览器对象
s = Service('../chromedriver.exe')
driver = webdriver.Chrome(service=s)
url = 'http://zeno-manager.xwkj.local/#/passport/login?sessionId=e168889d-264a-4a18-a08e-eb56e86965c5'
driver.maximize_window()
driver.get(url=url)
#name="ion-input-0"
driver.find_element(by=By.XPATH,value='//input[@class="ng-untouched ng-pristine ng-invalid ant-input ant-input-lg"]').send_keys('15010224947')
obj = driver.find_element(by=By.XPATH,value='//input[@type="password"]').send_keys("123456")
#v = obj.get_attribute('placeholder')
driver.find_element(by=By.XPATH,value="//button").click()
time.sleep(2)

driver.get('http://zeno-manager.xwkj.local/#/home/96307?1660722673974')

time.sleep(2)

eli = driver.find_element(by=By.XPATH,value='//a[@class="ng-star-inserted"]')


ActionChains(driver).click(eli).perform()

time.sleep(2)
# 如果是非 input 标签，则通过模拟按键操作的形式进行文件上传
ActionChains(driver).click(driver.find_element(by=By.CLASS_NAME,value='ant-upload')).perform()
time.sleep(2)
sh = win32com.client.Dispatch('WScript.shell')
sh.Sendkeys("E:\study\\22.mp4"+ '{ENTER}'+'\r\n')

time.sleep(20)
ActionChains(driver).click(driver.find_element(by=By.XPATH, value='//button[@class="list-btn ng-star-inserted ant-btn ant-btn-primary"]')).perform()
