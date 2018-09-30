from Page.page_setting import PageSetting
from Page.page_sms import PageSms
from Page.page_tel import PageTel


class PageIn():
    def __init__(self, driver):
        self.driver = driver

    def page_get_page_setting(self):
        return PageSetting(self.driver)

    def page_get_page_sms(self):
        return PageSms()

    def page_get_page_tel(self):
        return PageTel()