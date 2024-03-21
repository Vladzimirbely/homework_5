from selene import browser, be, have

def test_check_name_header():
    browser.element('h1').should(have.text('Practice Form'))

def test_enter_data():
    browser.element('#firstName').should(be.blank).type(('first name'))
    browser.element('#lastName').should(be.blank).type(('last name'))
    browser.element('#userEmail').should(be.blank).type(('test@test.test'))
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('[for="gender-radio-2"]').should(be.visible).click()
    browser.element('.react-datepicker-wrapper').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="2"]').click()
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1998"]').click()
    browser.element('.react-datepicker__day--002').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('label[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys('C:/Users/vladz/OneDrive/Desktop/homework_5/test/images/Screenshot_1.png')
    browser.element('#currentAddress').should(be.blank).type('Address')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').click()

    browser.element('.table').all('tr td:nth-child(2)').should(have.texts
        (
        'first name last name',
        'test@test.test',
        'Female',
        '1234567890',
        '02 March,1998',
        'Computer Science',
        'Music',
        'Screenshot_1.png',
        'Address',
        'Haryana Karnal'
    ))
