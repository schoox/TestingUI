from driver import Browser
from functions.eye import TheEye
from functions.pages import Page
from config import get_root_url, set_environment
from functions.actions import Element

def before_all(context):
    context.driver = Browser()
    context.eye = TheEye(context.driver)
    context.page = Page(context)
    context.domain = get_root_url(set_environment())
    context.element = Element(context)

def after_all(context):
    context.driver.close()
