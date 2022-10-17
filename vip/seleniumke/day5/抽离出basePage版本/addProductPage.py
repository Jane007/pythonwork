# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : addProductPage.py
# @ide     : PyCharm
# @time    : 2021/4/28 20:46
"""商品管理，添加商品页面"""

from basePage import BasePage
from selenium.webdriver.common.by import By


class AddProductPage(BasePage):

    def __init__(self):
        super().__init__()
        self.url = "http://120.55.190.222:38090/#/pms/addProduct"

    def product_classification_select_box(self):
        """商品分类下拉框, 外框"""
        return self.driver.find_element_by_css_selector("form > div:nth-child(1) .el-cascader__label")

    def product_classification_select_box_idx1(self, idx1):
        """商品分类下拉框, 一级分类"""
        return self.driver.find_element_by_css_selector("ul.el-cascader-menu > li:nth-child(%s)" % idx1)

    def product_classification_select_box_idx2(self, idx2):
        """商品分类下拉框, 二级分类"""
        return self.driver.find_element_by_css_selector("ul + ul.el-cascader-menu > li:nth-child(%s)" % idx2)

    def product_name_input_box(self):
        """商品名称输入框"""
        return self.driver.find_element_by_css_selector("label[for=\"name\"] + div input")

    def product_subtitle_input_box(self):
        """副标题输入框"""
        return self.driver.find_element_by_css_selector("label[for=\"subTitle\"] + div input")

    def product_brand_select_box(self):
        """商品品牌下拉框外框"""
        # return self.driver.find_element_by_css_selector("label[for=\"brandId\"] + div input")
        return self.get_element((By.CSS_SELECTOR, "label[for=\"brandId\"] + div input"))

    def product_brand_select_box_option(self, idx):
        """商品品牌下拉框, 一级分类"""
        return self.driver.find_element_by_css_selector("body > div:nth-child(8) ul > li:nth-child(%s)" % idx)

    def next_step_commodity_promotion_button_box(self):
        """下一步, 填写商品促销按钮"""
        return self.driver.find_element_by_xpath("//*[text()=\"下一步，填写商品促销\"]")

    def is_herald_box(self):
        """预告商品开关"""
        return self.driver.find_element_by_xpath("//*[text()=\"预告商品：\"]/..//span")

    def next_step_product_attribute_button_box(self):
        """下一步, 填写商品属性按钮"""
        return self.driver.find_element_by_xpath("//*[text()=\"下一步，填写商品属性\"]")

    def next_step_choose_product_related_button_box(self):
        """下一步, 选择商品关联按钮"""
        return self.driver.find_element_by_xpath("//*[text()=\"下一步，选择商品关联\"]")

    def submit_product_button_box(self):
        """完成, 提交商品按钮"""
        return self.driver.find_element_by_xpath("//*[text()=\"完成，提交商品\"]")

    def confirm_submission_box(self):
        return self.driver.find_element_by_css_selector(
            "[class=\"el-button el-button--default el-button--small el-button--primary \"]")


class AddProductPageAction(AddProductPage):

    def add_product_action(self, idx1, idx2, product_name, subtitle, brand_select_idx):
        self.to_page(1, self.url)
        # 点击商品分类下拉外框
        self.product_classification_select_box().click()
        # 选择一级分类
        self.product_classification_select_box_idx1(idx1).click()
        # 选择二级分类
        self.product_classification_select_box_idx2(idx2).click()
        # 输入商品名称
        self.product_name_input_box().send_keys(product_name)
        # 输入副标题
        self.product_subtitle_input_box().send_keys(subtitle)
        # 点击商品品牌下拉框外框
        self.product_brand_select_box().click()
        # 选择商品品牌一级分类
        self.product_brand_select_box_option(brand_select_idx).click()
        # 点击[下一步,填写商品促销]按钮
        self.next_step_commodity_promotion_button_box().click()
        # 点击是否预告商品开关
        self.is_herald_box().click()
        # 点击[下一步, 填写商品属性]按钮
        self.next_step_product_attribute_button_box().click()
        # 点击下一步, 选择商品关联按钮
        self.next_step_choose_product_related_button_box().click()
        # 点击完成,提交商品按钮
        self.submit_product_button_box().click()
        # 确认提交
        self.confirm_submission_box().click()


AddProductPageActionObj = AddProductPageAction()
