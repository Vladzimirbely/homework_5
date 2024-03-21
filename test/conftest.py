import pytest
from selene import browser, be, have

@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()
