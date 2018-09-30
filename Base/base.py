# 封装 公共方法
from selenium.webdriver.support.wait import WebDriverWait



class Base():
    def __init__(self, driver):
        self.driver = driver

    def base_get_element(self, loc, timeout=30, poll=0.5):
        driver = self.driver
        # 增加显示等待
        return WebDriverWait(driver, timeout=timeout, poll_frequency=poll).until(lambda x:x.find_element(*loc))

    def base_click(self, loc):
        self.base_get_element(loc).click()

    def base_input(self, loc, text):
        el = self.base_get_element(loc)
        el.clear()
        el.send_keys(text)