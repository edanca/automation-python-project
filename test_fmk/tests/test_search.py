from pytest import fixture

from test_fmk.pages.home import Home


class TestSearch:

    home = None

    @fixture(autouse=True)
    def before(self, browser):
        self.home = Home(browser)
        self.home.open()

    def test_search_2nd_iphone_2nd_page(self):
        self.home.search_input.input_text('iphone')
        self.home.search_btn.click()
