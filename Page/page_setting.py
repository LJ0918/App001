from Base.base import Base
import Page


class PageSetting(Base):
    # 点击 搜索
    # 输入文本
    # 点击返回
    def page_click_search(self):
        self.base_click(Page.setting_search_btn)

    def page_input(self, text):
        self.base_input(Page.setting_input_search, text)

    def page_click_back(self):
        self.base_click(Page.setting_back_btn)