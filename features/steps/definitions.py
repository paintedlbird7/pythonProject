from re import search
from behave import step
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# @step('Navigate to Google')
# def test(context):
#     driver = webdriver.Chrome()
#     driver.get('https://google.com')

#feature steps pass

@step('open eBay.com')
def open_ebay(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.get('https://ebay.com')

@step('In search field type "dress')
def search_for_some_item(context):
    search_field = context.driver.find_element('xpath', "//input[@aria-label = 'Search for anything']")
    search_field.send_keys('dress')
    sleep(3)

@step('Click the "Search" button')
def click_search(context):
    # button = context.driver.find_element('xpath', f"//input[@value ='Search']")
    button = context.driver.find_element('xpath', "//input[@value ='Search']")
    button.click()

# @step('Pick the first available from results page')
# def first_item(context):
    #first = context.driver.find_element('xpath', f"//"")
#     first = context.driver.find_element('xpath', "//'xpath', "")

@step('Click the "Sell" button')
def click_search(context):
    button = context.driver.find_element('xpath', "//li[@id ='gh-p-2']")
    button.click()
    sleep(4)
    print("clicked Sell")

@step('Click the "Daily Deals" button')
def click_search(context):
    button = context.driver.find_element('xpath', "//li[@id ='gh-p-1']")
    button.click()
    sleep(4)

@step('Click the "Gift Cards" button')
def click_search(context):
    button = context.driver.find_element('xpath', "//li[@id ='gh-p-6']")
    button.click()
    sleep(4)


@step('Click the "Help & Contact" button')
def click_search(context):
    button = context.driver.find_element('xpath', "//li[@id ='gh-p-3']")
    button.click()
    sleep(4)