from pytest import fixture

from test_fmk.pages.home import Home
from test_fmk.pages.product import Product
from test_fmk.pages.product_list import ProductList
from test_fmk.helpers.utils import switch_window


class TestSearch:

    home = None
    product = None
    product_list = None

    @fixture(autouse=True)
    def before(self, browser):
        self.home = Home(browser)
        self.product_list = ProductList(browser)
        self.product = Product(browser)

        self.home.open()
        self.home.perform_login()

    def test_search_2nd_iphone_2nd_page(self, browser):
        self.home.search_input.input_text('iphone')
        self.home.search_btn.click()

        self.product_list.scroll_down()
        self.product_list.page_two_btn.wait_for_element_present().click()
        self.product_list.product_list(elem_number=2).click()

        switch_window(browser, window_number=1)

        availability = self.product.items_available.get_text()
        quantity_available = int(availability.split(' ')[0])
        print(quantity_available)

        assert quantity_available > 0
