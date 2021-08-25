import logging
import time

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

from constans.base import BaseConstans
from constans.login_page import LoginPageConstants
from constans.profile_page import ProfilePageConstants
from helpers.base import BaseHelpers
from pages.profile_page import ProfilePage


def wait_until_ok(timeout, period=0.25):
    """Waiter"""

    def act_decorator(target_func):
        logger = logging.getLogger(__name__)

        def wrapper(*args, **kwargs):
            must_end = time.time() + timeout
            while True:
                try:
                    return target_func(*args, **kwargs)
                except (WebDriverException, AssertionError, TimeoutError) as error:
                    error_name = error if str(error) else error.__class__.__name__
                    logger.debug("Catch %s. Left %s seconds", error_name, (must_end - time.time()))
                    if time.time() >= must_end:
                        logger.warning("Waiting timed out after $s", timeout)
                        raise error
                    time.sleep(period)

        return wrapper

    return act_decorator


class LoginPage(BaseHelpers):
    """Store helpers for login page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = logging.getLogger(__name__)
        self.constants = LoginPageConstants

    @wait_until_ok(timeout=10)
    def click_sign_up_and_verify(self):
        """ Click Sign Up button and verify the result"""
        # Press register button
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.SIGN_UP_BUTTON_XPATH)
        self.log.info('Logged In')

        # 3. Verify result.
        assert self.driver.find_element(by=By.XPATH, value=ProfilePageConstants.SIGN_OUT_BUTTON_XPATH)

    def registration(self, username='', email='', password=''):
        """Helper for login to resource by registration for a new user with valid data"""
        # Go to the start page
        self.driver.get(BaseConstans.START_PAGE_URL)

        # Helper for fill fields
        base_helper = BaseHelpers(self.driver)

        # Fill username field
        base_helper.fill_input_field(by=By.XPATH, locator=self.constants.SIGN_UP_USERNAME_XPATH, value=username)

        # Fill email field
        base_helper.fill_input_field(by=By.XPATH, locator=self.constants.SIGN_UP_EMAIL_XPATH, value=email + '@gmail.com')

        # Fill password field
        base_helper.fill_input_field(by=By.XPATH, locator=self.constants.SIGN_UP_PASSWORD_XPATH, value=password)
        self.log.info('Filled required fields')

        # Press register button
        self.click_sign_up_and_verify()

        # Return Profile Page
        return ProfilePage(self.driver)

    def sign_in(self, username='', password=''):
        """Helper for Sign In"""
        base_helper = BaseHelpers(self.driver)

        # Type to field username (in 'Sign In' form) correct username
        base_helper.fill_input_field(by=By.XPATH, locator=self.constants.SIGN_IN_USERNAME_XPATH, value=username)
        self.log.info(f'Type login: "{username}"')

        # Type to field password (in 'Sign In' form) correct password
        base_helper.fill_input_field(by=By.XPATH, locator=self.constants.SIGN_IN_PASSWORD_XPATH, value=password)
        self.log.info(f'Type password: "{password}"')

        # Press "Sign In" button
        self.wait_and_click(locator_type=By.XPATH, locator=self.constants.SIGN_IN_BUTTON_XPATH)

        # Return Profile Page
        return ProfilePage(self.driver)
