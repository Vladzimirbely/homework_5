from selene import browser, be, have
import pytest

def test_check_name_header():
    browser.element('h1').should(have.text('Practice Form'))

