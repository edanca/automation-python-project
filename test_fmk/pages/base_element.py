from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement:
    def __init__(self, driver, locator, plural=False, wait=60):
        self.driver = driver
        self.locator = locator
        self.elem = None

        if not plural:
            self.wait_for_element_present(wait)
        else:
            self.wait_for_elements_present(wait)

    def wait_for_element_present(self, wait=60):
        self.elem = WebDriverWait(self.driver, wait).until(
            EC.visibility_of_element_located(self.locator)
        )
        return self.elem

    def wait_for_elements_present(self, wait=60):
        self.elem = WebDriverWait(self.driver, wait).until(
            EC.visibility_of_all_elements_located(self.locator)
        )
        return self.elem

    def input_text(self, text):
        self.elem.send_keys(text)

    def click(self, wait=60):
        self.elem = WebDriverWait(self.driver, wait).until(
            EC.element_to_be_clickable(self.locator)
        )
        self.elem.click()

    def get_text(self, wait=60):
        self.elem = WebDriverWait(self.driver, wait).until(
            EC.visibility_of_element_located(self.locator)
        )
        return self.elem.text
