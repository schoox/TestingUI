from behave import given, when, then

@given('I login as "{role}"')
def logi_as(context, role):
    context.role = role
    context.browser.driver.get(context.domain + "common/CSRF/getToken.php?email=panos@schoox.com")


@when('I go to Training Page Tab Curricula')
def go_to_training_tab_curricula(context):
    # case is the test name
    context.case = context.page.training_curricula(context.acad_id)
    print(context.case)


@when('I go to Training Page Tab Courses')
def go_to_training_tab_courses(context):
    context.case = context.page.training_courses(context.acad_id)


@when('I go to Training Page Tab Events')
def go_to_training_tab_events(context):
    context.case = context.page.training_events(context.acad_id)

@when('I go to Training Page Tab Bundles')
def go_to_training_tab_bundles(context):
    context.case = context.page.training_bundles(context.acad_id)


@when('I go to My Training Page Tab My Courses')
def go_to_training_tab_courses(context):
    context.case = context.page.my_training_courses(context.acad_id)


@when('I go to My Training Page Tab My Curricula')
def go_to_training_tab_courses(context):
    context.case = context.page.my_training_curricula(context.acad_id)


@when('I go to My Training Page Tab My Events')
def go_to_training_tab_events(context):
    context.case = context.page.my_training_events(context.acad_id)

@then('I will check the page')
def check_with_eye(context):
    context.eye.scroll_strict_mode(context.role)
