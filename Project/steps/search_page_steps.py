from behave import *

@given('I am on the https://jules.app/search/all page')
def step_impl(context):
    context.search_box_object.navigate_to_search_page()


@when('I insert "{something}" in the search box and hit Enter')
def step_impl(context, something):
    context.search_box_object.insert_search(something)

@then('I should have "{something}" in the search area')
def step_impl(context, something):
    context.search_box_object.check_search_item(something)
