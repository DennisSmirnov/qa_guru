import os

from selene import browser, have, be


def test_filling_from(browser_controller):
    browser.open('automation-practice-form')

    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    browser.element('#firstName').should(be.blank).click().type('Денис')
    browser.element('#lastName').should(be.blank).click().type('Смирнов')
    browser.element('#userEmail').should(be.blank).click().type('abc@bvg.ru')
    browser.element('label[for=gender-radio-1]').click()
    browser.element('#userNumber').should(be.blank).click().type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select > option[value="1992"]').click()
    browser.element('.react-datepicker__month-select > option[value="0"]').click()
    browser.element('.react-datepicker__day--001').click()
    browser.element('#subjectsInput').type('Acc')
    browser.element('.subjects-auto-complete__menu-list').element('//*[text()="Accounting"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()
    browser.element('#currentAddress').should(be.blank).click().type('Москва, ул. Пушкина, д. Колотушкина')
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Agra').press_enter()
    browser.element('#uploadPicture').send_keys(os.path.abspath("data\picha.jpg"))
    browser.element('#submit').click()

    browser.element('//table//td[text()="Student Name"]/../td[2]').should(have.exact_text('Денис Смирнов'))
    browser.element('//table//td[text()="Student Email"]/../td[2]').should(have.exact_text('abc@bvg.ru'))
    browser.element('//table//td[text()="Gender"]/../td[2]').should(have.exact_text('Male'))
    browser.element('//table//td[text()="Mobile"]/../td[2]').should(have.exact_text('1234567890'))
    browser.element('//table//td[text()="Date of Birth"]/../td[2]').should(have.exact_text('01 January,1992'))
    browser.element('//table//td[text()="Subjects"]/../td[2]').should(have.exact_text('Accounting'))
    browser.element('//table//td[text()="Hobbies"]/../td[2]').should(have.exact_text('Music'))
    browser.element('//table//td[text()="Picture"]/../td[2]').should(have.exact_text('picha.jpg'))
    browser.element('//table//td[text()="Address"]/../td[2]').should(
        have.exact_text('Москва, ул. Пушкина, д. Колотушкина'))
    browser.element('//table//td[text()="State and City"]/../td[2]').should(have.exact_text('Uttar Pradesh Agra'))
    browser.quit()
