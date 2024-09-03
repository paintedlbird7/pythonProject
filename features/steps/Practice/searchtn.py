from behave import *
from selenium import webdriver

@given('I got navigated to Home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")

# @when(u'I enter valid product in the Search box field')
# def step_impl(context):
#     context.driver.find_element(By.NAME, 'search').send_keys('Hp')
#
# @when(u'I click on Search button')
# def step_impl(context):
#     context.driver.find_element(By.XPATH, "//div[@id='search']//button").click()
#     print('I clicked on Search button')
#
# @then(u'Valid product should get displayed in Search results')
# def step_impl(context):
#     assert context.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
#     context.driver.quit()
#     print("Inside - Valid product should get displayed in Search results")

#TODO: fix errors













