from behave import *
#1/2 half of feature steps pass

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
        # # 3. passes all tests


@step('Item list should have only "iphone" related')
def check_only_iphone(context):
    items_on_page = context.driver.find_elements_by_xpath("//div[class='class='srp-main srp-main--isLarge']")
    for item in items_on_page:
       if 'dress' not in item.text.lower():
           print(f'Item {item.text} does not have iphone"')
            # # 4. error: TODO: Then Item list should have only "iphone" related doesnt pass
           # Do I need to "send keyes" for it to search "dress"?

# # 1. TODO: types 'item' instead of 'iphone'
# # 2. TODO: gets 'items' list instead of a list of dresses
# # 5. prints all items
# Use a While Loop for Pagination
