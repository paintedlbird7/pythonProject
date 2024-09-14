# from behave import *
# # from lxml.xslt import message
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# # completed
# @step('All items are "{item}" related')
# def check_all_items(context, item):
#     #uncomment for HW5
#     all_items = context.driver.find_elements('xpath', "//li[@class = 's-item s-item__pl-on-bottom' and contains(@id, 'item')]//span[@role = 'heading']")
#     # uncomment for HW7
#     # all_items = context.wait.until(EC.presence_of_all_elements_located(
#     #     (By.XPATH, "//li[@class = 's-item s-item__pl-on-bottom' and contains(@id, 'item')]//span[@role = 'heading']"),
#     #                                                      message='No items were found')
#
#     for every_item in all_items:
#         item_title = every_item.text
#         print(item_title)
#     # validate
#     if item.lower() not in item_title.lower(): #True
#         # same as print
#         # raise Exception(f'Following item not related to {item}: {item_title}')
#         print(f'Following item not related to {item}: {item_title}')
#
#
# @step('Item list should have only "iphone" related')
# def check_only_iphone(context):
#     items_on_page = context.driver.find_elements('xpath', "//div[class='srp-main srp-main--isLarge']")
#     for item in items_on_page:
#        if 'iphone' not in item.text.lower():
#            print(f'Item {item.text} does not have iphone"')
#
# # # 5. prints all items
# # Use a While Loop for Pagination
