from selenium.webdriver.common.by import By

from test_fmk.basis.base import Base

items_available = '.product-quantity-tip'


class Product(Base):

    @property
    def items_available(self):
        return self.get_base_element(By.CSS_SELECTOR, items_available)

    def get_product_availability(self):
        availability = self.items_available.get_text()
        quantity_available = int(availability.split(' ')[0])

        return quantity_available
