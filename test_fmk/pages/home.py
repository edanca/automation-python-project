from selenium.webdriver.common.by import By

from ..pages.base import Base

search_input = 'SearchText'
search_btn = '//input[@type="submit" and @class="search-button"]'


class Home(Base):
    @property
    def search_input(self):
        return self.get_base_element(By.NAME, search_input)

    @property
    def search_btn(self):
        return self.get_base_element(By.XPATH, search_btn)
