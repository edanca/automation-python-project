from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test_fmk.basis.base import Base

product_list = '.product-img'
page_two_btn = '//button[text()="2"]'


class ProductList(Base):

    def product_list(self, elem_number=0):
        return self.get_base_elements(By.CSS_SELECTOR, product_list, elem_number)

    @property
    def page_two_btn(self):
        return self.get_base_element(By.XPATH, page_two_btn)

    def scroll_down(self):
        ActionChains(self.driver) \
            .key_down(Keys.CONTROL) \
            .send_keys(Keys.END) \
            .key_up(Keys.CONTROL) \
            .perform()
