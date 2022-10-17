# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : basePage.py
# @ide     : PyCharm
# @time    : 2021/4/28 20:34

from mySettings import timeout, poll_time
from myDriver import Driver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time


class BasePage:

    def __init__(self):
        self.driver = Driver.get_driver()

    def get_element(self, locator):  # locator 格式 (By.ID, "kw")
        return WebDriverWait(
            # 传入浏览器对象
            driver=self.driver,
            # 传入最大超时时间
            timeout=timeout,
            # 传入轮询时间
            poll_frequency=poll_time).until(
            ec.visibility_of_element_located(locator)
        )

    def to_page(self, wait_time,url):
        time.sleep(wait_time)
        self.driver.get(url)
