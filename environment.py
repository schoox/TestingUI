from driver import Browser
from functions.eye import TheEye
from functions.pages import Page
from config import get_root_url, set_environment

def before_all(context):
    context.driver = Browser()
    context.eye = TheEye(context.driver)
    context.page = Page(context)
    context.domain = get_root_url(set_environment())


def after_all(context):
    context.driver.close()
