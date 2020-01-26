from os import environ
from pytest import fixture
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from time import sleep

env = environ.get('MY_ENV', 'local')


@fixture(scope='module')
def browser():
    browser = None
    if env == 'local':
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        browser = webdriver.Chrome(options=options)
    elif env == 'docker':
        sleep(3)
        url_selenium = 'http://chrome:4444/wd/hub'
        browser = webdriver.Remote(url_selenium, desired_capabilities=DesiredCapabilities.CHROME)

    yield browser

    if browser:
        browser.quit()
