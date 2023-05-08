from browser import Browser
from pages.login_page import LoginPage


def before_all(context):

    context.browser = Browser()
    context.login_page_object = LoginPage()


def after_all(context):

    context.browser.close()
