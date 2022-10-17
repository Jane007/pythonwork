# -*- coding:utf-8 -*-

from basePage import BasePage


class ProductLIstPage(BasePage):
    def __init__(self):
        super().__init__()
        self.url = "http://120.55.190.222:38090/#/pms/product"

    def first_tr_product_name_box(self):
        """商品列表的第一行商品的商品名称"""
        return self.driver.find_element_by_css_selector("tbody > :nth-child(1) > td:nth-child(4) p:nth-child(1)")


class ProductLIstPageAction(ProductLIstPage):
    pass


ProductLIstPageActionObj = ProductLIstPageAction()
