from dell import open_website
import time

def test_filter_check():
    browser = open_website()
    browser.implicitly_wait(10)
    products_menu = browser.find_element_by_css_selector('li[data-testid="umh_t1_1_Products"]')
    products_menu.click()
    laptops_menu = products_menu.find_element_by_css_selector('li[data-testid="umh_t1_1_t2_1_Laptops"]')
    laptops_menu.click()
    link = laptops_menu.find_element_by_css_selector('li[data-testid="umh_t1_1_t2_1_t3_1_For Home"]')
    link.click()

    select_filter(browser, "$800+")
    time.sleep(5)
    select_filter(browser, "1TB or more")

    # browser.find_element_by_id('productCategoryTiles-inspiron-laptops').click()
    # prices = browser.find_elements_by_css_selector('#refinerid-1 > li')
    # for price in prices:
    #     price.find_elements_by_css_selector('span[data-testid="anav_filter_refiner"]')

    # link = browser.find_element_by_css_selector('li[data-testid="umh_t1_1_Products"] > li[data-testid="umh_t1_1_t2_1_t3_1_For Home"] > a')
    # link.click()


def select_filter(browser, text):
    spans = browser.find_elements_by_css_selector('span[data-testid="anav_filter_refiner"]')
    the_span = next(filter(lambda s: s.text == text, spans))
    the_span.click()
