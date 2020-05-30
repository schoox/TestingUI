from behave import given, when, then

@given('I login as "{role}"')
def login_as(context, role):
    context.role = role
    context.browser.driver.get(context.domain + "common/CSRF/getToken.php?email=panos@schoox.com")


@when('I go to Manage Members Tab Employees')
def go_to_manage_members_employees(context):
    # case is the test name
    context.case = context.page.manage_members_employees(context.acad_id)
    print(context.case)


@when('I go to Manage Members Tab Past Employees')
def go_to_manage_members_past_employees(context):
    # case is the test name
    context.case = context.page.manage_members_past_employees(context.acad_id)
    print(context.case)


@when('I go to Manage Members Tab External Members')
def go_to_manage_members_external_members(context):
    # case is the test name
    context.case = context.page.manage_members_external_members(context.acad_id)
    print(context.case)


@when('I go to Manage Members Tab Past External Members')
def go_to_manage_members_past_external_members(context):
    # case is the test name
    context.case = context.page.manage_members_past_external_members(context.acad_id)
    print(context.case)


@then('I will check the page')
def check_with_eye(context):
    context.eye.scroll_strict_mode(context.role)
