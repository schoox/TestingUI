from behave import given, when, then


@given('I login as "{role}"')
def logi_as(context, role):
    context.role = role
    context.browser.driver.get(context.domain + "common/CSRF/getToken.php?email=panos@schoox.com")


@when('I go to Content Page')
def go_content_page(context):
    # case is the test name
    context.case = context.page.academy_library(context.acad_id)
    print(context.case)


# @when('I go to Training Page Tab Courses')
# def go_to_training_tab_courses(context):
#     context.case = context.page.training_courses(context.acad_id)


@then('I will check the page')
def check_with_eye(context):
    context.eye.scroll_strict_mode(context.role)
