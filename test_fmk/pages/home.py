from selenium.webdriver.common.by import By

from test_fmk.basis.base import Base
from test_fmk.config.constants import usr_email, usr_pass

search_input = 'SearchText'
search_btn = '//input[@type="submit" and @class="search-button"]'
user_account_icon = '.user-account-port'
sign_in_btn = '//a[@data-role="sign-link"]'

login_form_account = 'fm-login-id'  # ID
login_form_pass = 'fm-login-password'  # ID
login_form_btn = '//button[text()="Sign In"]'

iframe_login = 'alibaba-login-box'  # ID
iframe_login_id = iframe_login


class Home(Base):
    @property
    def search_input(self):
        return self.get_base_element(By.NAME, search_input)

    @property
    def search_btn(self):
        return self.get_base_element(By.XPATH, search_btn)

    @property
    def user_account_icon(self):
        return self.get_base_element(By.CSS_SELECTOR, user_account_icon)

    @property
    def sign_in_btn(self):
        return self.get_base_element(By.XPATH, sign_in_btn)

    @property
    def login_form_account(self):
        return self.get_base_element(By.ID, login_form_account)

    @property
    def login_form_pass(self):
        return self.get_base_element(By.ID, login_form_pass)

    @property
    def login_form_btn(self):
        return self.get_base_element(By.XPATH, login_form_btn)

    @property
    def iframe_login_id(self): return iframe_login_id

    @property
    def iframe_login(self):
        return self.get_base_element(By.ID, iframe_login)

    def perform_login(self):
        self.user_account_icon.click()
        self.sign_in_btn.click()

        self.iframe_login.wait_for_elements_present()
        self.driver.switch_to.frame(iframe_login_id)

        self.login_form_account.input_text(usr_email)
        self.login_form_pass.input_text(usr_pass)
        self.login_form_btn.click()
