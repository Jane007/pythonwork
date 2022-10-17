# -*- coding:utf-8 -*-

from basePage import BasePage


class ProductTypePage(BasePage):

    def __init__(self):
        super().__init__()
        self.page_url = "http://120.55.190.222:38090/#/pms/productAttr"

    def add_product_type_button_box(self):
        """添加商品类型按钮"""
        locator = "button.btn-add"
        return self.driver.find_element_by_css_selector(locator)

    def type_name_input_box(self):
        """添加商品类型弹窗, 类型名称输入框"""
        locator = ".el-dialog__body input.el-input__inner"
        return self.driver.find_element_by_css_selector(locator)

    def type_ico_upload_button(self):
        """添加商品类型弹窗, 分类图标, 文件上传, input 标签"""
        locator = "file"
        return self.driver.find_element_by_name(locator)

    def list_style_radio_button_box(self, index):
        """添加商品类型弹窗, 列表样式"""
        locator = "form > :nth-child(3)  .el-radio-group > :nth-child(%s)" % index
        return self.driver.find_element_by_css_selector(locator)

    def is_show_on_home_page_radio_button_box(self, index):
        """添加商品类型弹窗, 是否展示首页, 展示"""
        locator = "form > :nth-child(4)  .el-radio-group > :nth-child(%s)" % index
        return self.driver.find_element_by_css_selector(locator)

    def cancel_button_box(self):
        """添加商品类型弹窗, 取消按钮"""
        locator = "span > button:nth-child(1)"
        return self.driver.find_element_by_css_selector(locator)

    def confirm_button_box(self):
        """添加商品类型弹窗, 确定按钮"""
        locator = "span > button:nth-child(2)"
        return self.driver.find_element_by_css_selector(locator)

    def type_number(self, idx):
        """
        商品类型, 数据列表, 类型编号
        :param idx: 列表第几行
        :return:
        """
        return self.driver.find_element_by_css_selector("tbody > :nth-child(%s) > :nth-child(1) > div" % idx)

    def type_name(self, idx):
        """
        商品类型, 数据列表, 类型名称
        :param idx: 列表第几行
        :return:
        """
        return self.driver.find_element_by_css_selector("tbody > :nth-child(%s) > :nth-child(2) > div" % idx)

    def total_number(self):
        return self.driver.find_element_by_css_selector(".el-pagination__total")


class ProductTypePageAction(ProductTypePage):

    def add_product_type_action(self, type_name, img_path, list_style_index, is_show_on_home_page_index):
        # 点击添加商品类型按钮
        ProductTypePageActionObj.add_product_type_button_box().click()
        # 输入类型名称
        self.type_name_input_box().send_keys(type_name)
        # 上传分类图标
        if img_path is not None:
            self.type_ico_upload_button().send_keys(img_path)
        # 选择列表样式
        self.list_style_radio_button_box(list_style_index).click()
        # 选择是否展示在首页
        self.is_show_on_home_page_radio_button_box(is_show_on_home_page_index).click()
        # 点击确定按钮
        self.confirm_button_box().click()


ProductTypePageActionObj = ProductTypePageAction()

if __name__ == '__main__':
    import time

    ProductTypePageActionObj.to_page(ProductTypePageActionObj.page_url, 3)

    ProductTypePageActionObj.add_product_type_action("商品类型%s" % time.time(), None, 1, 1)
