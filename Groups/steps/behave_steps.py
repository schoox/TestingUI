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
def go_to_discussions(context):
    context.case = context.page.group_all_discussions(context.group_id)

@when('I go to Group Content Page')
def go_to_content(context):
    context.case = context.page.group_content(context.group_id)

@when('I go to Group Members Page')
def go_to_group_members(context):
    context.case = context.page.group_members(context.group_id)

@when('I go to Group Admins Page')
def go_to_group_admins(context):
    context.case = context.page.group_admins(context.group_id)

@when('I go to Edit Group Page')
def go_to_edit_group(context):
    context.case = context.page.edit_group(context.group_id)

@when('I go to Edit Image Page')
def go_to_edit_image(context):
    context.case = context.page.edit_image(context.group_id)

@when('I go to Polls Page')
def go_to_polls(context):
    context.case = context.page.polls(context.group_id)

@when('I go to Create Poll Page')
def go_to_create_poll(context):
    context.case = context.page.create_poll(context.group_id)

@when('I go to Manage Polls Page')
def go_to_manage_polls(context):
    context.case = context.page.manage_polls(context.group_id)

@when('I go to Individual Invite Page')
def go_to_individual_invite(context):
    context.case = context.page.individual_invite(context.acad_id, context.group_id)

@when('I go to Advanced Invite Page')
def go_to_advanced_invite(context):
    context.case = context.page.advanced_invite(context.group_id, context.acad_id)

@when('I go to Individual Registration Page')
def go_to_individual_registration(context):
    context.case = context.page.individual_registration(context.acad_id, context.group_id)

@when('I go to Advanced Registration Page')
def go_to_advanced_registration(context):
    context.case = context.page.advanced_registration(context.group_id, context.acad_id)

@then('I will check the page')
def check_with_eye(context):
    context.eye.scroll_strict_mode(context.role)
