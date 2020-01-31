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
        self.home.search_product('iphone')

        self.product_list.go_to_page(2)
        self.product_list.select_product_number(2)

        switch_window(browser, window_number=1)

        availability = self.product.get_product_availability()

        assert availability > 0
