from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


#complete
@step('In search field type the word "{item7}"')
def search_for_some_item7(context, item7):
    search_field7 = context.wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@aria-label = 'Search for anything']")),
    message='There is no search field')
    search_field7.send_keys(item7)

@step('Click "Search" button')
def click_search(context):
    context.driver.implicitly_wait(5)
    button = context.driver.find_element(By.XPATH, f"//input[@value='Search']")














#
# @step("open the site eBay.com")
# def open_ebay7(context):
#     context.driver.get(context.URL)

# @step("check landing {expected_title}")
# def check_landing(context, expected_title):
#     actual_title = context.driver.title
#     assert actual_title == expected_title, f"Expected {expected_title} but got {actual_title}"

#     button.click()
#
# @then("Pick the first available item from results page")
# def first_item(context):
#     item = context.driver.find_element('xpath', f"")
#     print("Then Pick the first available item from results page")


# @step("Item was added to the cart")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: And Item was added to the cart')
#
# @step('All items are "{item7}" related')
# def check_all_items(context, item7):
#     all_items = context.wait.until(EC.presence_of_all_elements_located(By.XPATH, "//li[@class = 's-item s-item__pl-on-bottom' and contains(@id, 'item')]//span[@role = 'heading']"),message='No items were found')
#
#     for every_item in all_items:
#         item_title = every_item.text
#
#     # validate
#     if item.lower() not in item_title.lower(): #True
#         print(f'Following item not related to {item}: {item_title}')
