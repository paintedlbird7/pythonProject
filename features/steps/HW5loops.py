from behave import *

# completed
@step('All items are "{item}" related')
def check_all_items(context, item):
    all_items = context.driver.find_elements('xpath', "//li[@class = 's-item s-item__pl-on-bottom' and contains(@id, 'item')]//span[@role = 'heading']")

    for every_item in all_items:
        item_title = every_item.text
        print(item_title)
    # validate
    if item.lower() not in item_title.lower(): #True
        # same as print
        # raise Exception(f'Following item not related to {item}: {item_title}')
        print(f'Following item not related to {item}: {item_title}')


@step('Item list should have only "iphone" related')
def check_only_iphone(context):
    items_on_page = context.driver.find_elements('xpath', "//div[class='srp-main srp-main--isLarge']")
    for item in items_on_page:
       if 'dress' not in item.text.lower():
           print(f'Item {item.text} does not have iphone"')
           # Do I need to "send keyes" for it to search "dress"?

# # 5. prints all items
# Use a While Loop for Pagination
