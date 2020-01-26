from selenium.webdriver.common.by import By

from test_fmk.basis.base import Base

item_quantity = '//input[@aria-valuemin]'


class Product(Base):

    @property
    def item_quantity(self):
        return self.get_base_element(By.XPATH, item_quantity)
