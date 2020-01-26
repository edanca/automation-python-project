from collections import namedtuple

Locator = namedtuple('Locator', ['by', 'value'])


def switch_window(driver, window_number=0):
    if len(driver.window_handles) > 1:
        window_after = driver.window_handles[window_number]
        driver.switch_to.window(window_after)
