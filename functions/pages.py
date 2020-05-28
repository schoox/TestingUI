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

    def __get_url(self, url):
        """
            go to page
        """

        url = self.conf.domain + url
        if self.driver.current_url != url:
            self.driver.get(url)