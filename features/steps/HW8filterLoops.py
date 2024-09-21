from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pprint import pprint as pp

# completed

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

# task: filters that are not directly displayed on the item page, should be verified
# 1.first thing to do is collect all items
# repeat same action over over again, looping all items
# 2. some actions repeated 50 -58 ttimes
# 3. open every item in a new tab
# 3.1 click or extract href and excute script

@step('All items should be related to "{spec_criteria}" value | "{spec_value}"')
def check_filters(context, spec_criteria, spec_value):
    # collect all items
    all_items = context.wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//li[@class = 's-item s-item__pl-on-bottom' and contains(@id, 'item')]")))
    # how to operate with handles
    main_page = context.driver.window_handles  # []
    # print(context.driver.window_handles) # []

    context.driver.switch_to.window()
    # 4. check that we do have the brand is on the item specs if not raise an exception or
    # 4.1 collect all errors, if errors raise-signal if anything is found
    # 4.2
    errors = []
    for item in all_items:
        # get to every item page
        ## get the destination link
        link_element = item.find_element('xpath', './/@[href]')
        link_title = item.find_element('xpath', ".//span[@role = 'heading']").text
        print(link_title)

        href = link_element.get_attribute('href')
        context.driver.execute_script(f"window.open ({href})")

        # switch to last window
        context.driver.current_window_handle(context.driver.window_handles[-1])
        # collect all item specs


        lbls_text = [l.text for l in context.wait.until((EC.presence_of_all_elements_located(By.XPATH, "//dt[@class = 'ux-labels-values__labels']")))]
        vals_text = [v.text for v in context.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//dd[@class = 'ux-labels-values__values']")))]


        lables_text = [lbl.text for lbl in context.wait(...)]
        lables_text = [x.text for x in context.wait.until(...)]

        item_specs = dict(zip(lbls_text, vals_text))
        pp(item_specs)

        for exp_f, exp_v in expected_specs.items():
            if exp_f not in item_specs.keys():
                errors.append(f'Item {link_title} does not have specification related to {exp_f}')
            elif exp_v.lower() != item_specs[exp_f].lower():
                errors.append(f'Items {link_title} has different {exp_f}.{item_specs[exp_f]} != {exp_v}')

        # validation

        # 4.2 get back to main content
        context.driver.close()
        context.driver.current_window_handle(main_page)

@step('All items should be related to following')
def all_items_many_filters_check(context):
    expected_specs = {}
    # expected_specs = {r['filter name']:r['value' for r in context.table]}

    for row in context.table:
        name = row['filter name']
        value = row['filter value']
        expected_specs[name] = value
        print(expected_specs)


