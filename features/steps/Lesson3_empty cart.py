from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()


@then('Verify Cart has 0 item(s)')
def verify_cart_count(context, expected_count):
    actual_count = context.driver.find_element(By.ID, 'nav-cart-count')
    assert expected_count == actual_count, f'Expected {expected_count}, but got {actual_count}'

driver.quit()