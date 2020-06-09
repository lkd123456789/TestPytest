from base.base import Base
import page

class PageSearch(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    #点击搜索图标
    def search_click_icon(self):
        self.click_element(page.search_click_icon)
    #输入信息
    def search_input_text(self,value):
        self.input_text(page.search_input_text,value)
    #截图
    def search_get_screenshot(self):
        self.get_screenshot()
    #点击返回按钮
    def search_click_back(self):
        self.click_element(page.search_click_back)