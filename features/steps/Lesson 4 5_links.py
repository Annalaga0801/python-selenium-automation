from selenium.webdriver.common.by import By
from behave import given, when, then

TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')


@given('Open Amazon BestSellers page')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/')


@when('Verify there are {expected_number_links} links')
def verify_links_count(context, expected_number_links):
    actual_links = context.driver.find_elements(*TOP_LINKS)
    assert len(actual_links) == int(expected_number_links), f' Expected {expected_number_links} matches {actual_links}'

