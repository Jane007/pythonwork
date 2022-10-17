# @Project : pythonwork
# @File    : autoupload.py
# @Author  : zhangjing
# @Time    : 2022/8/17 17:10
# @Software : Pycharm
# @Description :

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import win32com.client

services = Service('../chromedriver.exe')
driver = webdriver.Chrome(service=services)
driver.implicitly_wait(2)
driver.maximize_window()

class LoginPage:
    def __init__(self):
        self.driver = driver

    def get_url(self,url):
        self.driver.get(url)

    def input_user_name_box(self):
        return self.driver.find_element(by=By.XPATH,value='//input[@class="ng-untouched ng-pristine ng-invalid ant-input ant-input-lg"]')

    def input_password_box(self):
        return self.driver.find_element(by=By.XPATH,value='//input[@type="password"]')
    def login_button_action(self):
        return self.driver.find_element(by=By.XPATH,value="//button")


class LoginAction(LoginPage):
    def login_action(self):
        url = 'http://zeno-manager.xwkj.local/#/passport/login?sessionId=dc806c91-0dbd-4185-a6c8-303e6dc1c321'
        self.get_url(url)
        self.input_user_name_box().send_keys("15010224947")
        self.input_password_box().send_keys("123456")
        self.login_button_action().click()

class ListPage:
    def open_page(self):
        self.driver = driver
        self.url ='http://zeno-manager.xwkj.local/#/home/96307?1660722673974'
        self.driver.get(self.url)
        time.sleep(4)
        eli = self.driver.find_element(by=By.XPATH, value='//a[@class="ng-star-inserted"]');
        print(eli.get_attribute("style"))
        ActionChains(self.driver).click(eli).perform()
        time.sleep(2)


class UplaodFile():
    def __init__(self):
        self.driver = driver

    def upload(self,path='E:\study\\22.mp4'):
        time.sleep(5)
        ActionChains(self.driver).click(self.driver.find_element(by=By.CLASS_NAME, value='ant-upload')).perform()
        time.sleep(2)
        sh = win32com.client.Dispatch('WScript.shell')
        sh.Sendkeys(path + '{ENTER}' + '\r\n')
        time.sleep(5)
        ActionChains(self.driver).click(self.driver.find_element(by=By.XPATH,
                                                       value='//button[@class="list-btn ng-star-inserted ant-btn ant-btn-primary"]')).perform()


loginPageAction = LoginAction()
time.sleep(3)
loginPageAction.login_action()
time.sleep(3)
listPage = ListPage()
listPage.open_page()
time.sleep(5)
UplaodFile().upload('E:\study\\33.mp4')






