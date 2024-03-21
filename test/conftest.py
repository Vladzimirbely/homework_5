import pytest
from selene import browser, be, have

@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.open('/')

    yield

    browser.quit()
