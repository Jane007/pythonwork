# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : case3.py
# @ide     : PyCharm
# @time    : 2021/4/28 21:43

from prodtctTypePage import ProductTypePageActionObj
import time


class TestProductTypeCase:

    def test_add_product_type(self):
        # 访问到页面
        ProductTypePageActionObj.to_page(3, ProductTypePageActionObj.page_url)
        # 取到之前的总数
        total_before = ProductTypePageActionObj.total_number().text.split(" ")[1]
        time.sleep(3)
        # 添加一个商品类型
        ProductTypePageActionObj.add_product_type_action(str(time.time()), None, "1", "1")
        time.sleep(1)
        # 取到之后的总数
        total_after = ProductTypePageActionObj.total_number().text.split(" ")[1]

        assert int(total_before) == int(total_after) - 1
