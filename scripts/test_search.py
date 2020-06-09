import sys,os
sys.path.append(os.getcwd())

import pytest
from base.base_driver import BaseDriver
from page.page_search import PageSearch
from tools.read_search import ReadSearch

class TestSearch:

   def setup_class(self):
       self.driver=BaseDriver().base_driver()
       self.search=PageSearch(self.driver)
       self.search.search_click_icon()
   def teardown_class(self):
       self.search.search_click_back()
       self.driver.quit()
   @pytest.mark.parametrize("value",ReadSearch().read_search("search"))
   def test_search(self,value):
       self.search.search_input_text(value)




