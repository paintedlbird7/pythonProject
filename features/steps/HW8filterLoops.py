from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#
@step('In search field type "{item}"')
def search_for_some_item(context, item):
    search_field = context.driver.find_element('xpath', "//input[@aria-label = 'Search for anything']")
    search_field.send_keys(item)

@step('Filter "{filter_name}" option "{option}"')
def filter_items(context, filter_name, option):
    filter_option = context.driver.find_element('xpath',
                                                f"//li[@class = 'x-refine__main__list'][.//div[text() = '{filter_name}']]"
                                                f"//div[@class = 'x-refine__select__svg'][.//span[text() = '{option}']]//input")
    filter_option.click()

@step('All items should be related to "{spec_criteria}" value | "{spec_value}"')
def check_filters(context, spec_criteria, spec_value):
    #collect all items
    all_items = context.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@class = 's-item s-item__pl-on-bottom' and contains(@id, 'item')]//span[@role = 'heading']")))

    # store the page we are starting from
    main_page = context.driver.current_window_handle
    print(main_page)

    # how to operate with handles
    print(context.driver.window_handles) # []

    # for item in all_items:
        # get to every item page
        # collect all item specs
        # validation
