from driver import Browser
from functions.eye import TheEye
from functions.pages import Page
from config import get_root_url, set_environment

def before_all(context):
    context.driver = Browser()
    context.eye = TheEye(context.driver)
    context.page = Page(context)
    context.domain = get_root_url(set_environment())

    context.acad_id = 617024721
    # context.home_page       = HomePage()
    # context.search          = SearchResultsPage()
    # context.login_page      = LoginPage()
    # context.action          = Actions()
    # context.see_the_results = ResultsPage()
    # context.checkout        = CheckoutPage()
    # context.shipping        = ShippingPage()
    # context.payment         = PaymentPage()
    # context.check_order     = CheckOrderPage()


def after_all(context):
    context.driver.close()
