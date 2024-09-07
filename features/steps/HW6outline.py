from behave import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


@step("open eBay.com")
def open_ebay(context):
    context.driver.get(context.URL)

@step('In search field type "{item}"')
def search_for_some_item(context, item):
    search_field = context.driver.find_element('xpath', "//input[@aria-label = 'Search for anything'")
    search_field.send_keys(item)
    sleep(3)















# @step("goto {daily_deals}")

# def click_deals(context, daily_deals):
#     daily_deals = context.driver.find_element('xpath', f"//*[contains(@class, 'gh-') and text() = '{daily_deals}']")
#     daily_deals.click()
    #print("Clicked on the link  Daily Deals")


# @step('go to {anything}')
# def \
#         click_sell(context, anything):
#     # sell = context.driver.find_element('xpath', f"//a[@class, 'gh-p') and text() = {Sell}]")
#     btn = context.driver.find_element('xpath', f"//*[contains(@class, 'gh') and text() = '{anything}']")
#     btn.click()
#     sleep(4)
#     print("go to  empty_box")

# @step("check landing on {title}")
# def check_landing(context, title):
#     expected_title = context.driver.title
#     assert expected_title == title