from browser import Browser
from pages.login_page import LoginPage
from pages.search_page import SearchBox


def before_all(context):

    context.browser = Browser()
    context.login_page_object = LoginPage()
    context.search_box_object = SearchBox()


def after_all(context):

    context.browser.close()
