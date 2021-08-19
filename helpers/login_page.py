import logging

from selenium.webdriver.common.by import By

from constans.base import BaseConstans
from constans.login_page import LoginPageConstants
from helpers.base import BaseHelpers


class LoginPageHelpers(BaseHelpers):
    """
    Store helpers for login page
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = logging.getLogger(__name__)

    def login(self, username='', email='', password=''):
        """
        Helper for login to resource by registration for a new user with valid data
        """
        # Go to the start page
        self.driver.get(BaseConstans.START_PAGE_URL)
        # Helper for fill fields
        base_helper = BaseHelpers(self.driver)
        # Fill username field
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value=username)
        # Fill email field
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value=email + '@gmail.com')
        # Fill password field
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value=password)
        self.log.info('Filled required fields')
        # Press register button
        self.driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_BUTTON_XPATH).click()
        self.log.info('Logged In')
