from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

SEARCH_INPUT = (By.ID, "hubHelpSearchInput")
SEARCH_RESULT_TEXT = (By.CSS_SELECTOR, "h1.Cancel Items or Orders")


@given("open Amazon help search")
def open_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when("search for {search_query}")
def search_amazon(context, search_query):
    context.driver.find_element(*SEARCH_INPUT).send_keys(search_query)


@when("click Enter")
def search_click(context):
    search = driver.find_element(By.ID, 'hubHelpSearchInput')
    search.clear()
    search.send_keys('Cancel order', Keys.ENTER)


@then("verify {expected_result} result is present")
def verify_result(context, expected_result):
   actual_result = context.driver.find_element(*SEARCH_RESULT_TEXT).text
   assert expected_result == actual_result, f'Error!Actual text {actual_result} does not match expected {expected_result}'
