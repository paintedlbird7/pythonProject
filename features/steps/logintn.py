from behave import *

@given("I navigated to Login page")
def step_impl(context):

    print('INSIDE - Given I navigated to Login page')


@when("I enter valid email address and valid password into the field")
def step_impl(context):

    print('INSIDE - When I enter valid email address and valid password into the field')


@step("I click on Login button")
def step_impl(context):

    print('INSIDE - And I click on Login button')


@then("I should get logged in")
def step_impl(context):

    print('INSIDE - Then I should get logged in')


@when("I enter invalid email address and valid password into the field")
def step_impl(context):

    print('INSIDE - When I enter invalid email address and valid password into the field')


@then("I should get a proper warning message")
def step_impl(context):

    print('INSIDE - Then I should get a proper warning message')


@when("I enter valid email address and invalid password into the field")
def step_impl(context):

    print('INSIDE - When I enter valid email address and invalid password into the field')


@when("I enter invalid email address and invalid password into the field")
def step_impl(context):

    print('INSIDE - When I enter invalid email address and invalid password into the field')


@given("I got navigated to Login page")
def step_impl(context):

    print('INSIDE - Given I got navigated to Login page')


@when("I don't enter anything into the into the email and password fields")
def step_impl(context):

    print("INSIDE - When I don't enter anything into the into the email and password fields")