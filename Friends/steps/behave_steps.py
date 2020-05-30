from behave import given, when, then


@given('I login as "{role}"')
def logi_as(context, role):
    context.role = role
    context.browser.driver.get(context.domain + "common/CSRF/getToken.php?email=panos@schoox.com")


@when('I go to User Friends List')
def go_to_user_friends_list(context):
    context.case = context.page.user_friends_list(context.acad_id, context.user_id)


@then('I will check the page')
def check_with_eye(context):
    context.eye.scroll_strict_mode(context.role)

