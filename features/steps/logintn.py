from behave import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


@given("I navigated to Login page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
    # context.driver.get("https://tutorialsninja.com/demo/")
    # context.driver.find_element(By.XPATH, "//span[text()='My Account'").click()
    context.driver.find_element(By.LINK_TEXT, "Login").click()
    print('INSIDE - Given I navigated to Login page')
    sleep(10)


@when("I enter valid email address and valid password into the field")
def step_impl(context):

    print('INSIDE - When I enter valid email address and valid password into the field')


# @step("I click on Login button")
# def step_impl(context):
#
#     print('INSIDE - And I click on Login button')
#
#
# @then("I should get logged in")
# def step_impl(context):
#
#     print('INSIDE - Then I should get logged in')
#
#
# @when("I enter invalid email address and valid password into the field")
# def step_impl(context):
#
#     print('INSIDE - When I enter invalid email address and valid password into the field')
#
#
# @then("I should get a proper warning message")
# def step_impl(context):
#
#     print('INSIDE - Then I should get a proper warning message')
#
#
# @when("I enter valid email address and invalid password into the field")
# def step_impl(context):
#
#     print('INSIDE - When I enter valid email address and invalid password into the field')
#
#
# @when("I enter invalid email address and invalid password into the field")
# def step_impl(context):
#
#     print('INSIDE - When I enter invalid email address and invalid password into the field')
#
#
# @given("I got navigated to Login page")
# def step_impl(context):
#
#     print('INSIDE - Given I got navigated to Login page')
#
#
# @when("I don't enter anything into the into the email and password fields")
# def step_impl(context):
#
#     print("INSIDE - When I don't enter anything into the into the email and password fields")