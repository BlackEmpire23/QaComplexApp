import logging
from time import sleep

from selenium.webdriver.common.by import By

from constans.profile_page import ProfilePageConstants
from helpers.base import BaseHelpers
from pages.post_page import PostPage


class ProfilePage(BaseHelpers):
    """Store helpers for profile page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = logging.getLogger(__name__)
        self.constants = ProfilePageConstants

    def logout(self):
        """Click on 'Log Out' button"""
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.SIGN_OUT_BUTTON_XPATH)
        self.log.info('Logged out')

    def click_create_post(self):
        # Click on "Create Post" button
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.CREATE_POST_BUTTON_XPATH)
        self.log.info('Clicking on "Create Post" button.')

        return PostPage(self.driver)

    def find_post_by_search_field(self, username):
        # Click on search button
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.SEARCH_BUTTON_XPATH)
        self.log.info("CLicked on search button")

        # Type text to search field
        self.wait_until_element_find(locator_type=By.XPATH, locator=self.constants.SEARCH_INPUT_FIELD_XPATH)
        sleep(1)
        self.fill_input_field(by=By.XPATH, locator=self.constants.SEARCH_INPUT_FIELD_XPATH, value=username)
        self.log.info("Typed text to search")

    def verify_search(self, username):
        assert self.find_by_contains_text(text=username)
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.SEARCH_CLOSE_BUTTON_XPATH)
