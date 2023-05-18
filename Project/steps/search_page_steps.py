from behave import *

@given('I am on the https://jules.app/search/all page')
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
