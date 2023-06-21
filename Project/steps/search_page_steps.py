import time

from behave import *


@when("I login to the Jules app page")
def step_impl(context):
    context.search_box_object.login_to_desired_page()


@then('I am redirected to the search area')
def step_impl(context):
    context.search_box_object.check_login()


@given('I am on the Jules app page')
def step_impl(context):
    context.search_box_object.navigate_to_search_page()


@when('I insert "something" in the "all items" box and hit Enter')
def step_impl(context):
    context.search_box_object.insert_search_all_items()


@when('I insert "another" in the "my items" box and hit Enter')
def step_impl(context):
    context.search_box_object.insert_search_my_items()


@when('I insert "last" in the "external items" box and hit Enter')
def step_impl(context):
    context.search_box_object.insert_search_external_items()


@then('I should have "{message}" in the search area')
def step_impl(context, message):
    context.search_box_object.check_search_item(message)


@when('I press the notification button')
def step_impl(context):
    context.search_box_object.access_notification_bell()


@then('I can see the notification area message')
def step_impl(context):
    context.search_box_object.check_notif_message()


@when('I click on the notification type "{notif_name}"')
def step_impl(context, notif_name):
    context.search_box_object.click_notification(notif_name)


@then('I receive a notification with the message "{notification_message}"')
def step_impl(context, notification_message):
    context.search_box_object.check_disabled_message(notification_message)


@when('I press the question mark button')
def step_impl(context):
    context.search_box_object.click_question_mark()


@when('I select "{question_item}"')
def step_impl(context, question_item):
    context.search_box_object.select_question_mark_item(question_item)


@then('Another page opens with proper "{question_url}"')
def step_impl(context, question_url):
    context.search_box_object.check_question_item_url(question_url)


@when('I click on the person icon and select My account')
def step_impl(context):
    context.search_box_object.select_my_account()


@then('The number is saved in the phone field')
def step_impl(context):
    context.search_box_object.check_phone()