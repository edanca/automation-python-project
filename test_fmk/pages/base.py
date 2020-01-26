from ..config.constants import base_url
from .base_element import BaseElement
from test_fmk.helpers.locator import Locator

modal_close = '//a[@data-role="layer-close"]'


class Base:
    url = base_url

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def get_base_element(self, by, value):
        self.check_close_modal()
        locator = Locator(by, value)
        elem = BaseElement(self.driver, locator)
        return elem

    def check_close_modal(self):
        locator = Locator('xpath', modal_close)
        try:
            elem = BaseElement(self.driver, locator, wait=0.2)
            elem.click(wait=0.1)
        except Exception:
            pass
