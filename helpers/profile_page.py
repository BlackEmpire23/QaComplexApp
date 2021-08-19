import logging
from time import sleep

from selenium.webdriver.common.by import By

from constans.login_page import LoginPageConstants
from constans.profile_page import ProfilePage
from helpers.base import BaseHelpers


class ProfileHelpers(BaseHelpers):
    """
    Store helpers for profile page
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = logging.getLogger(__name__)

    def logout(self):
        self.driver.find_element_by_xpath(ProfilePage.SIGN_OUT_BUTTON_XPATH).click()
        sleep(1)

    def create_new_post(self, title, body):
        """
        Helper for creating a new post
        """
        base_helper = BaseHelpers(self.driver)

        # 1. Click on "Create Post" button
        self.driver.find_element_by_xpath(ProfilePage.CREATE_POST_BUTTON_XPATH).click()
        self.log.info('Clicking on "Create Post" button.')

        # 2. Fill "Title" field with any text.
        base_helper.fill_input_field(by=By.XPATH, locator=ProfilePage.POST_TITLE_XPATH, value=title)
        self.log.info('Filled "Title".')

        # 3. Fill "Body Content" with any text.
        base_helper.fill_input_field(by=By.XPATH, locator=ProfilePage.POST_BODY_CONTENT_XPATH, value=body)
        self.log.info('Filled "Body content".')

        # 4. Click on "Save New Post" button.
        self.driver.find_element_by_xpath(ProfilePage.POST_SAVE_BUTTON_XPATH).click()
        self.log.info('Creating a post.')

    def sign_in(self, username='', password=''):
        base_helper = BaseHelpers(self.driver)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_USERNAME_XPATH, value=username)
        self.log.info(f'Type login: "{username}"')

        # 3. Type to field password (in 'Sign In' form) correct password
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_PASSWORD_XPATH, value=password)
        self.log.info(f'Type password: "{password}"')

        # 4. Press "Sign In" button
        self.driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_BUTTON_XPATH).click()
