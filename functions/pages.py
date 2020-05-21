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

    def __get_url(self, url):
        """
            go to page
        """

        url = self.conf.domain + url
        if self.driver.current_url != url:
            self.driver.get(url)