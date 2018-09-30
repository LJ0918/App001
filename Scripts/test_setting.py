import os, sys

import allure

sys.path.append(os.getcwd())
import pytest
from  Base.get_driver import get_driver
from Page.page_in import PageIn
from RaedData.read_setting import ReadSetting


def get_data():
    datas = ReadSetting('setting_data.yaml').read_setting()
    arrs = []
    for i in datas.values():
        arrs.append(i.get('data'))
    return arrs


class TestSetting():

    def setup_class(self):
        # 初始化driver
        self.driver = get_driver('com.android.settings', '.Settings')
        # 实例化PageIn
        self.pagein = PageIn(self.driver)
        # 获取setting对象
        self.setting = self.pagein.page_get_page_setting()

    def teardown_class(self):
        # 关闭页面
        self.driver.quit()

    @pytest.mark.parametrize("text", get_data())
    @allure.step('1.设置页面，点击搜索按钮')
    @allure.step('2.设置页面，输入搜索内容')
    @allure.step('3.设置页面，点击返回按钮')
    def test_setting(self, text):
        # setting对象调用点击搜索方法
        allure.attach('搜索按钮','点击搜索，成功跳转')
        self.setting.page_click_search()
        # setting对象调用输入文本方法
        allure.attach('搜索框输入文本', '填写搜索内容，搜索成功')
        self.setting.page_input(text)
        # setting对象调用点击回退方法
        allure.attach('回退按钮', '点击回退，回退成功')
        self.setting.page_click_back()


