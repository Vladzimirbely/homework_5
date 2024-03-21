from selene import browser, be, have

def test_check_name_header():
    browser.element('h1').should(have.text('Practice Form'))

def test_enter_data():
    browser.element('#firstName').should(be.blank).type(('first name'))
    browser.element('#lastName').should(be.blank).type(('last name'))
    browser.element('#userEmail').should(be.blank).type(('test@test.test'))
    browser.element('[for="gender-radio-2"]').should(be.visible).click()
    browser.element('.react-datepicker-wrapper').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="2"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1998"]').click()
    browser.element('.react-datepicker__day--002').click()
