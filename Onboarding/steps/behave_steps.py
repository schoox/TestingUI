from behave import given, when, then


@given('I login as "{role}"')
def login_as(context, role):
    context.role = role
    context.browser.driver.get(context.domain + "common/CSRF/getToken.php?email=panos@schoox.com")


@when('I go to Onboarding Profiles')
def go_to_onboarding_profiles(context):
    # case is the test name
    context.case = context.page.manage_members_employees(context.acad_id)
    print(context.case)


@when('I go to Onboarding Templates')
def go_to_onboarding_templates(context):
    # case is the test name
    context.case = context.page.onboarding_templates(context.acad_id)
    print(context.case)


@then('I will check the page')
def check_with_eye(context):
    context.eye.scroll_strict_mode(context.role)
