from os import environ
from pytest import fixture
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


@fixture(scope='module')
def browser():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--incognito')
    # browser = webdriver.Chrome(options=options)
    # url_selenium = 'http://chrome:4444/wd/hub'
    browser = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)

    yield browser

    if browser:
        browser.quit()
