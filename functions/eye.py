from applitools.common import StitchMode, BatchInfo, MatchLevel
from applitools.selenium import Eyes
from functions import helpers

BATCH_NAME = "Test_Suite_" + helpers.get_date(9)


class TheEye(object):
    """
    Class for handling applitools screenshot tests.
    """

    viewport_size = {'width': 1536, 'height': 710}
    app_name = "Schoox"
    batch_info = BatchInfo(BATCH_NAME)

    def __init__(self, driver):
        """
        Set driver.
        """

        self.driver = driver.driver

    def __get_api_key(self):
        """
        Return api key.
        """

        return "irAQhgXDKnvXhsDdgBKyVDSDfDvpdoMoENpD0i8dQBI110"

    def __configuration(self, config_case):
        """
        Set up the Eye configuration.
        :param config_case: integer, set the configuration case.
                            Case 1: Strict mode, scrolling along the whole window.
                                    Mismatches due to blinking cursor artifacts are eliminated.
                                    The scrollbar is hidden.
                                    StitchMode: CSS
        """

        eyes = Eyes()
        eyes.configure.set_api_key(self.__get_api_key())

        eyes.batch = self.batch_info
        if config_case == 1:
            # set the overlap between sub-images when a scrolled window is stitched in pixels
            eyes.stitch_overlap = 45 # height of menu
            eyes.configure.set_force_full_page_screenshot(True)
            # StitchMode.Scroll did not work
            eyes.configure.set_stitch_mode(StitchMode.CSS)
            eyes.configure.set_hide_scrollbars(True)
            eyes.configure.set_hide_caret(True)
            eyes.configure.set_match_level(MatchLevel.STRICT)
        return eyes

    def scroll_strict_mode(self, role, test_name, config_case=1):
        """
        This function will get the window screenshot, based on the configuration case that has
        been set by the test. The page should be hit by your test first.
        """

        eyes = self.__configuration(config_case)
        eyes.open(driver=self.driver, app_name=self.app_name,
                  test_name=test_name,
                  viewport_size=self.viewport_size)

        try:
            eyes.check_window('As_' + role)
            helpers.pause_for(1)
            eyes.close()
            # If we use a runner + de tha skasei to test
            # eyes.close_async()
        finally:
            # get_all_test_results method, if runner is used
            eyes.abort_if_not_closed()
