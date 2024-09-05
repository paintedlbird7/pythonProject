from behave import *

use_step_matcher("re")


@given("I navigated to Register page")
def step_impl(context):

    print('INSIDE - Given I navigated to Register page')


@when("I enter mandatory fields")
def step_impl(context):

    print('INSIDE - When I enter mandatory fields')


@step("I click on Continue button")
def step_impl(context):

    print('INSIDE - And I click on Continue button')


@then("Account should get created")
def step_impl(context):

    print('INSIDE - Then Account should get created')


@when("I enter all fields")
def step_impl(context):

    print('INSIDE - When I enter all fields')


@when("I enter details into all fields except email fields")
def step_impl(context):

    print('INSIDE - When I enter details into all fields except email fields')


@step("I enter existing accounts into email fields")
def step_impl(context):

    print('INSIDE - And I enter existing accounts into email fields')


@then("Proper warning message informing about duplicate account should be displayed")
def step_impl(context):

    print('INSIDE - Then Proper warning message informing about duplicate account should be displayed')


@when("I don't enter anything in the fields")
def step_impl(context):

    print("INSIDE -  When I don't enter anything in the fields")


@then("Proper warning messages for every mandatory field should be displayed")
def step_impl(context):

    print('INSIDE - Then Proper warning messages for every mandatory field should be displayed')