import time

from behave import *


@given('I am on the https://jules.app page')
def step_impl(context):
    context.login_page_object.navigate_to_login_page()


@when('I click the login button')
def step_impl(context):
    context.login_page_object.click_login_button()
    time.sleep(2)


@then('I can login into the application and I am redirected to the https://jules.app/search/all page')
def step_impl(context):
    context.login_page_object.loged_in_page()


@then('I can not login into the application and I receive "{error_message}" error')
def step_impl(context, error_message):
    context.login_page_object.check_error_message(error_message)


@when("I insert username '{utilizator_gresit}' and password '{parola}'")
def step_impl(context, utilizator_gresit, parola):
    context.login_page_object.insert_username(utilizator_gresit)
    context.login_page_object.insert_password(parola)


@then("I can not login into the application and I receive '{no_user}' error")
def step_impl(context, no_user):
    context.login_page_object.no_user_error(no_user)


@when('I insert username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page_object.insert_username(username)
    context.login_page_object.insert_password(password)
