import pytest
from selene import browser, be, have

@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.open('https://demoqa.com/automation-practice-form')

    yield

    browser.quit()
