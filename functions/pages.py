"""
    All pages for navigation
"""
class Page():
    """
        Class to get to page
    """

    def __init__(self, conf):
        """
            Page constructor
        """
        self.conf = conf
        self.driver = conf.browser.driver

    def home_page(self):
        """
            return page key
        """
        self.driver.get()
        key = "Home Page"

        return key

    def my_training(self):
        """
            return page key
        """
        self.driver.get()
        key = "My Training"

        return key

    def training_curricula(self, acad_id):
        """
            return page key
        """

        key = "Training Curricula"
        self.__get_url("academies/tp.php?acadId=" + str(acad_id) + "#?priority=2")
        return key

    def training_courses(self, acad_id):
        """
            return page key
        """

        key = "Training Courses"
        self.__get_url("academies/courses.php?acadId=" + str(acad_id))
        return key

    def training_events(self, acad_id):
        """
            return page key
        """

        key = "Training Events"
        self.__get_url("academies/events.php?acadId=" + str(acad_id) + "#?dateadded=1")
        return key

    def training_bundles(self, acad_id):
        """
            return page key
        """

        key = "Training Bundles"
        self.__get_url("academies/bundles.php?acadId=" + str(acad_id))
        return key

    def my_training_courses(self, acad_id):
        """
            return page key
        """

        key = "My Training Courses"
        self.__get_url("academies/courses.php?acadId=" + str(acad_id) + "&mine=1")
        return key

    def my_training_curricula(self, acad_id):
        """
            return page key
        """

        key = "My Training Curricula"
        self.__get_url("academies/tp.php?acadId=" + str(acad_id) + "&mine=1")
        return key

    def my_training_events(self, acad_id):
        """
            return page key
        """

        key = "My Training Events"
        self.__get_url("academies/events.php?acadId=" + str(acad_id) + "&mine=1")
        return key

    def academy_library(self, acad_id):
        """
            return page key
        """
        key = "Academy Library"
        self.__get_url("academies/library2.php?acadId="+ str(acad_id) + "#?dateadded=1")
        return key

    def academy_groups(self, acad_id):
        """
            return page key
        """
        key = "Academy Groups"
        self.__get_url("academies/groups.php?acadId=" + str(acad_id))
        return key

    def create_new_group(self, acad_id):
        """
            return page key
        """
        key = "Create Group"
        self.__get_url("groups/addgroup.php?acadId=" + str(acad_id))
        return key

    def group_wall(self, group_id):
        """
            return page key
        """
        key = "Group Wall"
        self.__get_url("groups/wall.php?group_id=" + str(group_id))
        return key

    def group_all_discussions(self, group_id):
        """
            return page key
        """
        key = "Group All Discussions"
        self.__get_url("groups/discussions.php?group_id=" + str(group_id))
        return key

    def group_content(self, group_id):
        """
            return page key
        """
        key = "Group Content"
        self.__get_url("groups/content.php?group_id=" + str(group_id))
        return key

    def group_members(self, group_id):
        """
            return page key
        """
        key = "Group Members"
        self.__get_url("groups/people.php?group_id=" + str(group_id))
        return key

    def group_admins(self, group_id):
        """
            return page key
        """
        key = "Group Admins"
        self.__get_url("groups/admins.php?group_id=" + str(group_id))
        return key

    def edit_group(self, group_id):
        """
            return page key
        """
        key = "Edit Group"
        self.__get_url("groups/addgroup.php?group_id=" + str(group_id))
        return key

    def edit_image(self, group_id):
        """
            return page key
        """
        key = "Edit Image"
        self.__get_url("groups/image.php?group_id=" + str(group_id))
        return key

    def polls(self, group_id):
        """
            return page key
        """
        key = "Polls"
        self.__get_url("groups/polls/polls.php?group_id=" + str(group_id))
        return key

    def create_poll(self, group_id):
        """
            return page key
        """
        key = "Create Poll"
        self.__get_url("groups/polls/index.php?group_id=" + str(group_id))
        return key

    def manage_polls(self, group_id):
        """
            return page key
        """
        key = "Manage Polls"
        self.__get_url("groups/polls/manage.php?group_id=" + str(group_id))
        return key

    def individual_invite(self, acad_id, group_id):
        """
            return page key
        """
        key = "Send Individual Invitation"
        self.__get_url("groups/invites/individual_group.php?acadId=" + str(acad_id) +
                       " &group_id=" + str(group_id))
        return key

    def advanced_invite(self, group_id, acad_id):
        """
            return page key
        """
        key = "Send Advanced Invitation"
        self.__get_url("groups/invites/advanced_group.php?group_id=" + str(group_id) + "&acadId="
                       + str(acad_id))
        return key

    def individual_registration(self, acad_id, group_id):
        """
            return page key
        """
        key = "Individual Registration"
        self.__get_url("groups/add_members/individual_group.php?acadId=" + str(acad_id) +
                       " &group_id=" + str(group_id))
        return key

    def advanced_registration(self, group_id, acad_id):
        """
            return page key
        """
        key = "Advanced Registration"
        self.__get_url("groups/add_members/advanced_group.php?group_id=" + str(group_id) +
                       "&acadId=" + str(acad_id))
        return key

    def manage_members_employees(self, acad_id):
        """
            return page key
        """
        key = "Manage Members Employees"
        self.__get_url("academies/panel/members2.php?acadId=" + str(acad_id))
        return key

    def manage_members_past_employees(self, acad_id):
        """
            return page key
        """
        key = "Manage Members Past Employees"
        self.__get_url("academies/panel/pastmembers.php?acadId=" + str(acad_id))
        return key

    def manage_members_external_members(self, acad_id):
        """
            return page key
        """
        key = "Manage Members External Members"
        self.__get_url("academies/panel/customers.php?acadId=" + str(acad_id))
        return key

    def manage_members_past_external_members(self, acad_id):
        """
            return page key
        """
        key = "Manage Members External Members"
        self.__get_url("academies/panel/pastcustomers.php?acadId=" + str(acad_id))
        return key

    def add_users_employees(self, acad_id):
        """
            return page key
        """
        key = "Add Users Employees"
        self.__get_url("academies/panel/import/index.php?acadId=" + str(acad_id))
        return key

    def add_users_external_members(self, acad_id):
        """
            return page key
        """
        key = "Add Users External Members"
        self.__get_url("academies/panel/import/external.php?acadId=" + str(acad_id))
        return key

    def onboarding_profiles(self, acad_id):
        """
            return page key
        """
        key = "Onboarding Profiles"
        self.__get_url("academies/panel/onboarding/index.php?acadId=" + str(acad_id))
        return key

    def onboarding_templates(self, acad_id):
        """
            return page key
        """
        key = "Onboarding Templates"
        self.__get_url("academies/panel/onboarding/template.php?acadId=" + str(acad_id))
        return key

    def user_friends_list(self, acad_id, user_id):
        """
            return page key
        """
        key = "User Friends List"
        self.__get_url("academies/friends.php?acadId=" + str(acad_id) + "&user=" + str(user_id))
        return key


    def __get_url(self, url):
        """
            go to page
        """

        url = self.conf.domain + url
        if self.driver.current_url != url:
            self.driver.get(url)
