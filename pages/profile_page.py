import logging

from selenium.webdriver.common.by import By

from constans.profile_page import ProfilePageConstants as ProfileConstants
from helpers.base import BaseHelpers


class ProfilePage(BaseHelpers):
    """Store helpers for profile page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = logging.getLogger(__name__)
        self.constants = ProfileConstants

    def logout(self):
        """Click on 'Log Out' button"""
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.SIGN_OUT_BUTTON_XPATH)

    def create_new_post(self, title, body):
        """Helper for creating a new post"""
        base_helper = BaseHelpers(self.driver)

        # 1. Click on "Create Post" button
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.CREATE_POST_BUTTON_XPATH)
        self.log.info('Clicking on "Create Post" button.')

        # 2. Fill "Title" field with any text.
        base_helper.fill_input_field(by=By.XPATH, locator=self.constants.POST_TITLE_XPATH, value=title)
        self.log.info('Filled "Title".')

        # 3. Fill "Body Content" with any text.
        base_helper.fill_input_field(by=By.XPATH, locator=self.constants.POST_BODY_CONTENT_XPATH, value=body)
        self.log.info('Filled "Body content".')

        # 4. Click on "Save New Post" button.
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.POST_SAVE_BUTTON_XPATH)
        self.log.info('Creating a post.')
