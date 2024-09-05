import item
from behave import *

# completed
@step('I have "{v1}" and "{v2}" "{v3}" "{v4}"')
def test(context, v1, v2, v3, v4):
    print(v1)
    print(v2)
    print(v3)
    print(v4)

@given("the text as a variable")
def test_text(context):
    my_var = context.text
    print(my_var)
    #print(context.text)


@given("Table as a variable")
def test_table(context):
    my_var = context.table
    print(my_var)

    print(my_var.headings)
    print(my_var.rows)

    #Loops
bag_items = ["apple", "orange", "carrot"]
for items in bag_items:
    print(f'unloading the {item}')





























