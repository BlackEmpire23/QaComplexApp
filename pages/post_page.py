import logging

from selenium.webdriver.common.by import By

from constans.post_page import PostConstants
from constans.profile_page import ProfilePageConstants
from helpers.base import BaseHelpers


class PostPage(BaseHelpers):
    """Store helpers for Post page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = logging.getLogger(__name__)
        self.constants = PostConstants

    def create_new_post(self, title, body):
        """Helper for creating a new post"""

        # 1. Fill "Title" field with any text.
        self.fill_input_field(by=By.XPATH, locator=self.constants.POST_TITLE_XPATH, value=title)

        # 2. Fill "Body Content" with any text.
        self.fill_input_field(by=By.XPATH, locator=self.constants.POST_BODY_CONTENT_XPATH, value=body)

        # 3. Click on "Save New Post" button.
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.POST_SAVE_BUTTON_XPATH)
        self.log.info('Creating a post.')

    def verify_post(self, username, title):
        """Verify a new post"""
        self.wait_and_click(locator_type=By.XPATH,
                            locator=ProfilePageConstants.MY_PROFILE_BUTTON_XPATH.format(lower_username=username))
        self.verify_message(xpath=ProfilePageConstants.POST_NAMES_XPATH, text=title)
        text = self.driver.find_elements_by_xpath(ProfilePageConstants.POST_NAMES_XPATH)
        assert len(text) == 1
        assert text[0].text == title
