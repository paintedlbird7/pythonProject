from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given("I launch Chrome browser")
def step_impl(context):
    context.driver = webdriver.Chrome()
    print("Chrome launched")

@when("I open orange HRM Homepage")
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com")
    print("Open Homepage")

@step('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element_by_id("username").send_keys(user)
    context.driver.find_element_by_id("password").send_keys(pwd)
    print("Creds entered")

@step("Click on login button")
def step_impl(context):
    context.driver.find_element_by("").click()
    print("Login clicked")


@then("User must successfully login to the Dashboard page")
def step_impl(context):
    text = context.driver.find_element_by_xpath("//header/div[1]/div[1]/span[1]/h6[1]").text
    assert text == "Dashboard"
    context.driver.close()
    print("Successfully logged in")
