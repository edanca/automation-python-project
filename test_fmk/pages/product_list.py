from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test_fmk.basis.base import Base

product_list = '.product-img'


class ProductList(Base):

    def product_list(self, elem_number=0):
        return self.get_base_elements(By.CSS_SELECTOR, product_list, elem_number)

    def page_number_locator(self, number):
        return f'//button[text()="{number}"]'

    def scroll_down(self):
        ActionChains(self.driver) \
            .key_down(Keys.CONTROL) \
            .send_keys(Keys.END) \
            .key_up(Keys.CONTROL) \
            .perform()

    def go_to_page(self, page_number):
        self.scroll_down()
        page_two_elem = self.get_base_element(By.XPATH, self.page_number_locator(page_number))
        page_two_elem.click()

    def select_product_number(self, product_number):
        self.product_list(product_number).click()
