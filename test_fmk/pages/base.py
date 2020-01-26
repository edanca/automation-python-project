from ..config.constants import base_url
from .base_element import BaseElement
from test_fmk.helpers.locator import Locator


class Base:
    url = base_url

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def get_base_element(self, by, value):
        locator = Locator(by, value)
        elem = BaseElement(self.driver, locator)
        return elem
