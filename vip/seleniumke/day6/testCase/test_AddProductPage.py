# -*- coding:utf-8 -*-

from addProductPage import AddProductPageActionObj as APP
from productListPage import ProductLIstPageActionObj as PLP
import time


def testAddProductCase():
    product_name = "%s" % time.time()

    # 添加一个商品
    APP.add_product_action("1", "1", product_name, product_name, 1)
    # 进入商品列表页面
    PLP.to_page(3, PLP.url)
    # 获取商品列表，第一个商品的商品名称
    first_product_name = PLP.first_tr_product_name_box().text

    assert product_name == first_product_name
