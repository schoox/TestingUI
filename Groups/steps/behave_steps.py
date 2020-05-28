from behave import given, when, then

@given('I login as "{role}"')
def logi_as(context, role):
    context.role = role
    context.browser.driver.get(context.domain + "common/CSRF/getToken.php?email=panos@schoox.com")

@when('I go to Academy Groups Page')
def go_to_academy_groups_tab(context):
    context.case = context.page.academy_groups(context.acad_id)

@when('I go to Create New Group Page')
def go_to_create_new_group(context):
    context.case = context.page.create_new_group(context.acad_id)

@when('I go to Group Wall Page')
def go_to_group_wall(context):
    context.case = context.page.group_wall(context.group_id)

@when('I go to Group All Discussions Page')
def go_to_group_wall(context):
    context.case = context.page.group_all_discussions(context.group_id)

@then('I will check the page')
def check_with_eye(context):
    context.eye.scroll_strict_mode(context.role)
