# from behave import *
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
# from webdriver_manager.chrome import ChromeDriverManager
#
# @step("open the site eBay.com")
# def open_ebay2(context):
#     context.driver.get(context.URL)
#
# # @step('In search field type the word "{item2}"')
# # def search_for_some_item2(context, item2):
# #     search_field2 = context.driver.find_element('xpath', "//input[@aria-label = 'Search for anything']")
# #     search_field2.send_keys(item2)
# #     sleep(3)
#
# @step("check landing {expected_title}")
# def check_landing(context, expected_title):
#     actual_title = context.driver.title
#     assert actual_title == expected_title, f"Expected {expected_title} but got {actual_title}"
#
#
#
# # @then("check landing on Daily Deals on eBay | Best deals and Free Shipping")
# # def step_impl(context):
# #     print("Then check landing on Daily Deals on eBay | Best deals and Free Shipping")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # @step("Pick the first available item from results page")
# # def first_available(context):
# #     item2 = context.driver.find_element(By.XPATH, f"")
#
# # @step("goto {daily_deals}")
#
# # def click_deals(context, daily_deals):
# #     daily_deals = context.driver.find_element('xpath', f"//*[contains(@class, 'gh-') and text() = '{daily_deals}']")
# #     daily_deals.click()
#     #print("Clicked on the link  Daily Deals")
#
#
# # @step('go to {anything}')
# # def \
# #         click_sell(context, anything):
# #     # sell = context.driver.find_element('xpath', f"//a[@class, 'gh-p') and text() = {Sell}]")
# #     btn = context.driver.find_element('xpath', f"//*[contains(@class, 'gh') and text() = '{anything}']")
# #     btn.click()
# #     sleep(4)
# #     print("go to  empty_box")
#
# # @step("check landing on {title}")
# # def check_landing(context, title):
# #     expected_title = context.driver.title
# #     assert expected_title == title
