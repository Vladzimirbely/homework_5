from selene import browser, be, have
import pytest

def test_check_name_header():
    browser.element('h1').should(have.text('Practice Form'))

def test_enter_data():
    browser.element('#firstName').should(be.blank).type(('first name'))
    browser.element('#lastName').should(be.blank).type(('last name'))
    browser.element('#userEmail').should(be.blank).type(('test@test.test'))
