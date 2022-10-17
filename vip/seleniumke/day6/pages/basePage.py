# -*- coding:utf-8 -*-
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from mySettings import timeout, poll_time
from utils.myDriver import Driver
import win32com.client
import time


class BasePage:

    def __init__(self):
        self.driver = Driver.get_driver()

    def get_element(self, locator):
        """
        封装一个显示等待函数
        :param locator: (By.ID, "kw")
        :return:
        """
        return WebDriverWait(
            # 传入浏览器驱动对象
            driver=self.driver,
            # 传入超时时间
            timeout=timeout,
            # 传入轮询时间
            poll_frequency=poll_time
        ).until(ec.visibility_of_element_located(locator))

    def to_page(self, wait_time, url):
        time.sleep(wait_time)
        self.driver.get(url)

    def upload_img(self, ele, wait_time, ing_path):
        ele.click()
        time.sleep(wait_time)


if __name__ == '__main__':
    x = BasePage()
