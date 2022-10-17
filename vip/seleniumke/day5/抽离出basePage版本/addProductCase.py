# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : addProductCase.py
# @ide     : PyCharm
# @time    : 2021/4/28 21:33
import time

from addProductPage import AddProductPageActionObj as APP
from productLIstPage import ProductLIstPageActionObj as PLP


def addProductCase():
    product_name = "%s" % time.time()

    # 添加一个商品
    APP.add_product_action("1", "1", product_name, product_name, 1)
    # 进入商品列表页面
    PLP.to_page(3, PLP.url)
    # 获取商品列表，第一个商品的商品名称
    first_product_name = PLP.first_tr_product_name_box().text

    print(product_name)
    print(first_product_name)
    if product_name == first_product_name:
        print("测试通过")
    else:
        print("测试失败")


addProductCase()
