from selenium import webdriver


def open_website():
    browser = webdriver.Chrome('C:/Users/vsapr/Downloads/chromedriver_win32/chromedriver.exe')
    browser.get('https://www.dell.com/en-us')
    return browser




