# from behave import *
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
#
# #completed
# @step('In search field type "{item}"')
# def search_for_some_item(context, item):
#     search_field = context.driver.find_element('xpath', "//input[@aria-label = 'Search for anything']")
#     search_field.send_keys(item)
#     sleep(10)
#
# @step('Filter "{filter_name}" option "{option}"')
# def filter_items(context, filter_name, option):
#     filter_option = context.driver.find_element('xpath',
#                                                 f"//li[@class = 'x-refine__main__list'][.//div[text() = '{filter_name}']]"
#                                                 f"//div[@class = 'x-refine__select__svg'][.//span[text() = '{option}']]//input")
#     filter_option.click()
#     sleep(10)
#
