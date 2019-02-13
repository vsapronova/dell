from dell import open_website


def test_search():
    browser = open_website()
    browser.find_element_by_id('search-input').send_keys('Desktop')
    browser.find_element_by_css_selector('#search-form > button').click()
    browser.implicitly_wait(10)
    result = browser.find_element_by_id('relatedCategories-selectCategory-GamingLaptopsDesktops')
    assert result.text == 'Gaming Laptops & Desktops'
