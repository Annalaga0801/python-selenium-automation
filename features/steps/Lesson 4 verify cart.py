from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
SEARCH_INPUT_MAIN = (By.ID, 'twotabsearchtextbox')
SEARCH_INPUT_HELP = (By.ID, 'hubHelpSearchInput')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
SEARCH_RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
CART_PAGE = (By.ID, 'nav-cart-count')
CART_ITEM = (By.XPATH, "//span[@class='a-truncate-cut']")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_word}')
def search_amazon(context, search_word):
    context.driver.find_element(*SEARCH_INPUT_MAIN).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()


@when('Click on the first item')
def click_first_item(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@when('Store item name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Product name: {context.product_name}')


@when('Click Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_CART_BTN).click()


@when('Open Cart page')
def open_cart(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=sw_gtc')


@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART_PAGE).text
    assert expected_count == actual_text, f'Expected {expected_count}, but got {actual_text}'


@when('Verify cart has correct item')
def verify_correct_item(context, expected_item):
    actual_result = context.driver.find_element(*CART_ITEM).text
    assert expected_item == actual_result, f'Expected {expected_item}, but got {actual_result}'


