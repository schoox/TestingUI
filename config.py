import time

CLASS_ID = ""
DRIVER = "C:\Python38/chromedriver.exe"

# this should be updated when we are going to add it on QA
QA_HOSTNAME = ""
ENV = "local"

def set_environment(env=True):
    """
    env = True OR
    env = 1 OR
    env = "develop" / "www" / "any_string_for_subdomain"
    """

    return env

def get_root_url(subdomain, domain="schoox.com", protocol="https://"):
    """
    :param subdomain: get the value from set_enviroment
    :param domain: for ultipro.com etc.
    :param protocol: currently schoox works only https
    """

    if isinstance(subdomain, bool):
        subdomain = "www"
    elif isinstance(subdomain, int):
        # clear 1 for staging.schoox.com
        subdomain = str(subdomain) if subdomain != 1 else ""
        subdomain = "staging" + subdomain

    root_url = protocol + subdomain + "." + domain + "/"

    return root_url


def assert_true_output(self, expr, msg=""):
    """
        Check that the expression is true.
        If not, take screenshot, grab the html, store them to the defined output_folder
        and raise failure exception
    """

    if not expr:
        prevent = False
        time.sleep(2)

        # html
        page_html_filename = CLASS_ID + '_' + 'page_html'

        # screenshot
        screenshot_name = CLASS_ID + '_' + 'screenshot'

        if ENV != "local":
            # important! DO NOT FORGET PERMISSIONS
            var = '/var/www/'
            linux_folder_path = 'testrail/TestingIntegration/failure_output/'
            host = "http://" + QA_HOSTNAME + "/"
            screenshot_path = var + linux_folder_path + screenshot_name + '.png'
            screenshot_path_link = host + linux_folder_path + screenshot_name + '.png'
            page_html_path = var + linux_folder_path + page_html_filename + '.txt'
            page_html_path_link = host + linux_folder_path + page_html_filename + '.txt'

            # save files
            self.wd.get_screenshot_as_file(screenshot_path)
            with open(page_html_path, 'w') as file: #pylint: disable=redefined-builtin
                file.write(self.element.get_html("//*").encode('utf-8'))

            # print paths to console
            msg += "\n\n---------------"
            msg += "\nFailure screenshot output: " + screenshot_path_link
            msg += "\nFailure page html output: " + page_html_path_link
            msg += "\n---------------\n\n"

        if prevent:
            return

        custom_assert(self, msg)
        time.sleep(3)

def custom_assert(self, msg):
    """
        If you are here, the test is gonna fail
    """

    raise self.failureException(msg)


def get_path(context, before="feature"):
    """
    Get the test name from the path of the test and return it.
    before="all"
    before="feature"
    before="scenario"
    before="step"
    """
    path = ""
    if before == "all":
        path = context._stack[0]['config'].paths[0]
    elif before == "feature":
        path = context._stack[0]["feature"].location.filename
    # Get the test name from the path, eg. C:/.../Training_curricula => Training curricula
    test_name = path.split('/')[-1].split('.')[0].replace("_", " ")

    return test_name

def set_before_feature(context, acad_id, group_id=None, case=1):
    """
        return the context
        case:1 -> set for UI testing/applitools
        case:2 -> set for functional test
        case:3 -> set for API cases
    """

    from driver import Browser
    from functions.eye import TheEye
    from functions.pages import Page

    if case == 1:
        context.browser = Browser()
        context.browser.open()
        context.eye = TheEye(context.browser.driver)
        context.eye.open_eye(get_path(context))
        context.page = Page(context)
        context.domain = get_root_url(set_environment())

    context.acad_id = acad_id
    if group_id is not None:
        context.group_id = group_id

    return context

def set_after(context, case=1):
    """
        case:1 -> set for UI testing/applitools
        case:2 -> set for functional test
        case:3 -> set for API cases
    """

    if case == 1:
        context.browser.close()
        context.eye.close_eye()
    elif case == 2:
        context.browser.close()
    else: #case 3, API doesn't need
        pass
