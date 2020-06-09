from datetime import time
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver=driver

    #查找元素
    def find_element(self,loc,time=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=time,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    #查找元组
    def find_elements(self,loc,time=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=time,poll_frequency=poll).until(lambda x:x.find_elements(*loc))
    #点击元素
    def click_element(self,loc):
        self.find_element(loc).click()
    #输入数据
    def input_text(self,loc,value):
        elem=self.find_element(loc)
        elem.clear()
        elem.send_keys(value)
    #截图
    def get_screenshot(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y-%m-%d-%H-%M-%S")))