from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# completed
@given('I got navigated to Home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")

@when(u'I enter valid product into the Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, 'search').send_keys('Hp')
sleep(7)

@when(u'I click on Search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='search']//button").click()
    print('I clicked on Search button')
sleep(7)

@then(u'Valid product should get displayed in Search results')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    context.driver.quit()
    print("Inside - Valid product should get displayed in Search results")
sleep(7)

#STARTS search tests
@when("I enter invalid product into the Search box field")
def step_impl(context):
    context.driver.find_element(By.NAME, 'search').send_keys('Honda')
    print('INSIDE - When I enter invalid product into the Search box field')


@step("Proper message should be displayed in Search results")
def step_impl(context):
    expected_text = "There is no product that matches the search criteria."
    assert context.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p")\
    .text.__eq__(expected_text)
    context.driver.quit()
    print('INSIDE -: And proper message should be displayed in Search results')



@when("I don't enter anything into the Search box field")
def step_impl(context):
    context.driver.find_element(By.NAME, 'search').send_keys('')
    print('INSIDE - When I don\'t enter anything into the Search box field')







