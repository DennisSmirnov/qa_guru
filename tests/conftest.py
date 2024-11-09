import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='session')
def browser_controller():
    browser.config.base_url = 'https://demoqa.com/'
    driver_options = webdriver.FirefoxOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.window_width = 1280
    browser.config.window_height = 720
    yield
    browser.quit()
