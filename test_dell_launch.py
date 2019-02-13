from selenium import webdriver


def test_dell_launch():
    browser = webdriver.Chrome('C:/Users/vsapr/Downloads/chromedriver_win32/chromedriver.exe')
    browser.get('https://www.dell.com/en-us')
    browser.find_element_by_id('signin-button').click()
    browser.find_element_by_css_selector('button.signin').click()
    email = browser.find_element_by_id('EmailAddress')
    email.send_keys('vn@gmail.com')
    password = browser.find_element_by_id('Password')
    password.send_keys('Vngmailcom1')
    browser.find_element_by_id('sign-in-button').click()



