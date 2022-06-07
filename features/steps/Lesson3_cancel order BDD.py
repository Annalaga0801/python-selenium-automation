from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then


@given('Open Amazon Help page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Search for {search_word}')
def search_input(context, search_word):
    search = context.driver.find_element(By.ID, 'hubHelpSearchInput')
    search.send_keys('Cancel order')


@when('click Enter')
def click_enter(context):
    search = context.driver.find_element(By.ID, 'hubHelpSearchInput')
    search.send_keys(Keys.Enter)

@then('Verify search results for {search_word} are shown')
    def verify_search_result(context, search_word):
    actual_result = context.driver.find_element(By.XPATH, "//div[contains(@class, 'help-cont')]/h1").text
    expected_result = 'Cancel Items or Orders'
    assert expected_result == actual_result, f'Expected{expected_result} does not match {actual_result}'

driver.quit()