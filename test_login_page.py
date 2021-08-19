import random
import string
from time import sleep

from selenium.webdriver.common.by import By

from conftest import BaseTest
from selenium import webdriver
import pytest
from constans.base import BaseConstans
from constans.login_page import LoginPageConstants
from constans.profile_page import ProfilePage
from helpers.base import BaseHelpers
from helpers.login_page import LoginPageHelpers
from helpers.profile_page import ProfileHelpers


class TestLoginPage(BaseTest):

    @pytest.fixture(scope='class')
    def driver(self):
        driver = webdriver.Chrome(executable_path=BaseConstans.DRIVER_PATH)
        yield driver
        driver.close()

    def test_username_on_registration_filed(self, driver):

        """
        Validation for registration field "Username":
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Type to field 1 or 2 symbols(letters or numbers).
        3. Clear this field and type 3 or more symbols with special symbol(for ex: @$%_ ^&*).
        4. Clear this field and type name which is already exists(for ex: 123).
        5. Clear this field and type more than 30 symbols(letters or numbers).
        6. Clear this field, type some text then clear this field """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)

        # Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # 2. Type to field 1 or 2 symbols(letters or numbers).
        text_2_chars = random.choice(string.ascii_letters) + str(random.randint(1, 9))
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value=text_2_chars)
        # Check alert text
        base_helper.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_USERNAME_3_CHARS_TEXT)
        self.log.info('Alert "Username must be at least 3 characters." appeared.')

        # 3. Clear this field and type 3 or more symbols with special symbol(for ex: @$%_ ^&*).
        text_with_chars_and_symbol = ''
        for i in range(3):
            text_with_chars_and_symbol += random.choice(string.ascii_letters)
            text_with_chars_and_symbol += random.choice(string.punctuation)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value=text_with_chars_and_symbol)
        sleep(2)
        # Check alert text
        base_helper.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH,
                                   text=LoginPageConstants.ALERT_USERNAME_ONLY_LET_AND_DIG_TEXT)
        self.log.info('Alert "Username can only contain letters and numbers." appeared.')

        # 4. Clear this field and type name which is already exists(for ex: 123).
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value='123')
        # Check alert text
        base_helper.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_USERNAME_ALREADY_TAKEN_TEXT)
        self.log.info('Alert "That username is already taken." appeared.')

        # 5. Clear this field and type more than 30 symbols(letters or numbers)."""
        text_30_chars = ''
        for i in range(16):
            text_30_chars += random.choice(string.ascii_letters)
            text_30_chars += str(random.randint(1, 9))
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value=text_30_chars)
        # Check alert text
        base_helper.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_USERNAME_MAX_LENGTH_TEXT)
        self.log.info('Alert "Username cannot exceed 30 characters." appeared')

        # 6. Clear this field, type some text then clear this field
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value='abc')
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        # Check alert text
        base_helper.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_USERNAME_3_CHARS_TEXT)
        self.log.info('Alert "Username must be at least 3 characters." appeared ')

    def test_email_on_registration_field(self, driver):
        """
        Validation for field "Email".
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Type to field invalid email (for ex:email without '@mail.com') - try different combinations.
        """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # Type to field invalid email (for ex: email without "@mail.com") - try different combinations.
        # 'Email' without @mail.com
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value='ergqerg')

        # Check alert text
        base_helper.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_EMAIL_VALID_EMAIL_TEXT)
        self.log.info('Alert for invalid email appeared')

        # 'Email' without mail.com
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value='asd@')

        # Check alert text
        base_helper.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_EMAIL_VALID_EMAIL_TEXT)
        self.log.info('Alert for invalid email appeared')

        # Empty 'Email' after fill email
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value='asd@')
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH)

        # Check alert text
        base_helper.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_EMAIL_VALID_EMAIL_TEXT)
        self.log.info('Alert for invalid email appeared')

    def test_password_for_registration_form(self, driver):

        """
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Type to field "Password" from 1 to 11 any symbols.
        3. Type to field "Password" more than 50 any symbols.
        4. Type to field "Password" any text then clear this field
        """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # 2. Type to field "Password" from 1 to 11 any symbols.
        password_text = ''
        for i in range(random.randint(1, 11)):
            password_text += random.choice(string.ascii_letters)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value=password_text)
        # Check alert text
        base_helper.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_PASSWORD_MIN_LENGTH_TEXT)
        self.log.info('Alert "Password must be at least 12 characters." appeared')

        # 3. Type to field "Password" more than 50 any symbols.
        password_text = ''
        for i in range(random.randint(50, 100)):
            password_text += random.choice(string.ascii_letters)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value=password_text)
        # Check alert text
        base_helper.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_PASSWORD_MAX_LENGTH_TEXT)
        self.log.info('Alert "Password cannot exceed 50 characters" appeared')

        # 4. Type to field "Password" any text then clear this field
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value='123')
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        # Check alert text
        base_helper.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_PASSWORD_MIN_LENGTH_TEXT)
        self.log.info('Alert "Password must be at least 12 characters." appeared')

    def test_successful_registration(self, driver):
        """
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Finish registration with valid data
        3. Verify result.
        4. Sign out
        """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)
        login_helper = LoginPageHelpers(driver)

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')
        # 2. Finish registration with valid data
        username, email, password = login_helper.user_data()
        login_helper.login(username=username, email=email, password=password)
        # 3. Verify result.
        base_helper.verify_message(xpath=ProfilePage.HELLO_MESSAGE_XPATH, text=ProfilePage.HELLO_MESSAGE_TEXT.format(
            lower_username=username.lower()))
        self.log.info('Checking login string')
        # 4. Sign out
        profile_helper = ProfileHelpers(driver)
        profile_helper.logout()

    def test_successful_sign_in(self, driver):
        """
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Finish registration with valid data
        3. Sign Out.
        4. Sign In.
        5. Verify result.
        6. Sign out
        """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)
        login_helper = LoginPageHelpers(driver)
        profile_helper = ProfileHelpers(driver)
        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')
        # 2. Finish registration with valid data
        username, email, password = login_helper.user_data()
        login_helper.login(username=username, email=email, password=password)
        # 3. Sign Out.
        profile_helper.logout()
        # 4. Sign In.
        profile_helper.sign_in(username=username, password=password)
        # 5. Verify result.
        base_helper.verify_message(xpath=ProfilePage.HELLO_MESSAGE_XPATH, text=ProfilePage.HELLO_MESSAGE_TEXT.format(
            lower_username=username.lower()))
        self.log.info('Checking login string')
        # 6. Sign out
        profile_helper = ProfileHelpers(driver)
        profile_helper.logout()

    def test_correct_username_and_empty_password_for_sign_in(self, driver):
        """
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Fill "Username" field with correct data and keep field "Password" empty and press "Sign In" button.
        3. Verify result.
        """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)
        profile_helpers = ProfileHelpers(driver)

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')
        # 2. Fill "Username" field with correct data and keep field "Password" empty and press "Sign In" button.
        profile_helpers.sign_in(username='123')
        sleep(1)
        # 3. Verify result.
        base_helper.verify_message(xpath=LoginPageConstants.SIGN_IN_ALERT_XPATH, text=LoginPageConstants.INVALID_SIGN_IN_MESSAGE_TEXT)
        self.log.info("Error message appeared")

    def test_incorrect_username_and_password_for_sign_in(self, driver):
        """
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Sign In with incorrect "Username" and "Password".
        3. Verify result.
        """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)
        profile_helpers = ProfileHelpers(driver)

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')
        # 2. Sign In with incorrect "Username" and "Password".
        profile_helpers.sign_in(username='efg@#', password='123qweasdzcz!@')
        # 3. Verify result.
        sleep(1)
        base_helper.verify_message(xpath=LoginPageConstants.SIGN_IN_ALERT_XPATH, text=LoginPageConstants.INVALID_SIGN_IN_MESSAGE_TEXT)
        self.log.info("Error message appeared")

    def test_valid_username_and_invalid_password_for_sign_in(self, driver):
        """
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Sign In with correct "Username" and incorrect "Password".
        3. Verify result.
        """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)
        profile_helpers = ProfileHelpers(driver)

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # 2. Sign In with correct "Username" and incorrect "Password".
        profile_helpers.sign_in(username='123', password='123qwer')
        # 3. Verify result.
        sleep(1)
        base_helper.verify_message(xpath=LoginPageConstants.SIGN_IN_ALERT_XPATH, text=LoginPageConstants.INVALID_SIGN_IN_MESSAGE_TEXT)
        self.log.info("Error message appeared")
