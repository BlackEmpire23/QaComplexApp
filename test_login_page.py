"""Store tests related to login page"""
import random
import string

from selenium.webdriver.common.by import By

from conftest import BaseTest
from constans.login_page import LoginPageConstants
from constans.profile_page import ProfilePageConstants
from helpers.base import BaseHelpers


class TestLoginPage(BaseTest):

    def test_username_on_registration_filed(self, start_page):
        """
        Validation for registration field "Username":
        1. Type to field 1 or 2 symbols(letters or numbers).
        2. Clear this field and type 3 or more symbols with special symbol(for ex: @$%_ ^&*).
        3. Clear this field and type name which is already exists(for ex: 123).
        4. Clear this field and type more than 30 symbols(letters or numbers).
        5. Clear this field, type some text then clear this field - checking empty fields.
        """
        # 1. Type to field 1 or 2 symbols(letters or numbers).
        start_page.fill_input_field(by=By.XPATH,
                                    locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH,
                                    value=random.choice(string.ascii_letters) + str(random.randint(1, 9)))
        # Check alert text
        start_page.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_USERNAME_3_CHARS_TEXT)
        self.log.info('Alert "Username must be at least 3 characters." appeared.')

        # 2. Clear this field and type 3 or more symbols with special symbol(for ex: @$%_ ^&*).
        text_with_chars_and_symbol = ''
        for i in range(3):
            text_with_chars_and_symbol += random.choice(string.ascii_letters)
            text_with_chars_and_symbol += random.choice(string.punctuation)

        start_page.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value=text_with_chars_and_symbol)
        # Check alert text
        start_page.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH,
                                  text=LoginPageConstants.ALERT_USERNAME_ONLY_LET_AND_DIG_TEXT)
        self.log.info('Alert "Username can only contain letters and numbers." appeared.')

        # 3. Clear this field and type name which is already exists(for ex: 123).
        start_page.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value='123')
        # Check alert text
        start_page.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_USERNAME_ALREADY_TAKEN_TEXT)
        self.log.info('Alert "That username is already taken." appeared.')

        # 4. Clear this field and type more than 30 symbols(letters or numbers)."""
        text_30_chars = ''
        for i in range(16):
            text_30_chars += random.choice(string.ascii_letters)
            text_30_chars += str(random.randint(1, 9))
        start_page.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value=text_30_chars)
        # Check alert text
        start_page.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_USERNAME_MAX_LENGTH_TEXT)
        self.log.info('Alert "Username cannot exceed 30 characters." appeared')

        # 5. Clear this field, type some text then clear this field - checking empty fields.
        start_page.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value='abc')
        start_page.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        # Check alert text
        start_page.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_USERNAME_3_CHARS_TEXT)
        self.log.info('Alert "Username must be at least 3 characters." appeared ')

    def test_email_on_registration_field(self, start_page):
        """
        Validation for field "Email".
        1. Type to field invalid email (for ex:email without '@mail.com') - try different combinations.
        """
        # Type to field invalid email (for ex: email without "@mail.com") - try different combinations.

        # 'Email' without @mail.com
        start_page.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value='ergqerg')
        # Check alert text
        start_page.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_EMAIL_VALID_EMAIL_TEXT)
        self.log.info('Alert for invalid email appeared')

        # 'Email' without mail.com
        start_page.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value='asd@')
        # Check alert text
        start_page.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_EMAIL_VALID_EMAIL_TEXT)
        self.log.info('Alert for invalid email appeared')

        # Empty 'Email' after fill email
        start_page.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value='asd@')
        start_page.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH)
        # Check alert text
        start_page.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_EMAIL_VALID_EMAIL_TEXT)
        self.log.info('Alert for invalid email appeared')

    def test_password_for_registration_form(self, start_page):
        """
        1. Type to field "Password" from 1 to 11 any symbols.
        2. Type to field "Password" more than 50 any symbols.
        3. Type to field "Password" any text then clear this field
        """
        # 1. Type to field "Password" from 1 to 11 any symbols.
        password_text = ''
        for i in range(random.randint(1, 11)):
            password_text += random.choice(string.ascii_letters)
        start_page.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value=password_text)
        # Check alert text
        start_page.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_PASSWORD_MIN_LENGTH_TEXT)
        self.log.info('Alert "Password must be at least 12 characters." appeared')

        # 2. Type to field "Password" more than 50 any symbols.
        password_text = ''
        for i in range(random.randint(50, 100)):
            password_text += random.choice(string.ascii_letters)
        start_page.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value=password_text)
        # Check alert text
        start_page.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_PASSWORD_MAX_LENGTH_TEXT)
        self.log.info('Alert "Password cannot exceed 50 characters" appeared')

        # 3. Type to field "Password" any text then clear this field
        start_page.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value='123')
        start_page.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        # Check alert text
        start_page.verify_message(xpath=LoginPageConstants.SIGN_UP_ALERT_XPATH, text=LoginPageConstants.ALERT_PASSWORD_MIN_LENGTH_TEXT)
        self.log.info('Alert "Password must be at least 12 characters." appeared')

    def test_successful_registration(self, start_page, logout):
        """
        1. Finish registration with valid data
        2. Verify result.
        """
        # 1. Finish registration with valid data
        username, email, password = BaseHelpers.user_data(start_page)
        profile_page = start_page.registration(username=username, email=email, password=password)

        # 2. Verify result.
        profile_page.verify_message(xpath=ProfilePageConstants.HELLO_MESSAGE_XPATH, text=ProfilePageConstants.HELLO_MESSAGE_TEXT.format(
            lower_username=username.lower()))
        self.log.info('Checking login string')

    def test_successful_sign_in(self, start_page, logout):
        """
        1. Finish registration with valid data
        2. Sign Out.
        3. Sign In.
        4. Verify result.
        """
        self.log.info('Entering to the page')
        # 1. Finish registration with valid data
        username, email, password = BaseHelpers.user_data(start_page)
        profile_page = start_page.registration(username=username, email=email, password=password)

        # 2. Sign Out.
        profile_page.logout()

        # 3. Sign In.
        start_page.sign_in(username=username, password=password)

        # 4. Verify result.
        profile_page.verify_message(xpath=ProfilePageConstants.HELLO_MESSAGE_XPATH, text=ProfilePageConstants.HELLO_MESSAGE_TEXT.format(
            lower_username=username.lower()))
        self.log.info('Checking Sign In string')

    def test_correct_username_and_empty_password_for_sign_in(self, start_page):
        """
        1. Fill "Username" field with correct data and keep field "Password" empty and press "Sign In" button.
        2. Verify result.
        """
        # 1. Fill "Username" field with correct data and keep field "Password" empty and press "Sign In" button.
        start_page.sign_in(username='123')

        # 2. Verify result.
        start_page.verify_message(xpath=LoginPageConstants.SIGN_IN_ALERT_XPATH, text=LoginPageConstants.INVALID_SIGN_IN_MESSAGE_TEXT)
        self.log.info("Error message appeared")

    def test_incorrect_username_and_password_for_sign_in(self, start_page):
        """
        1. Sign In with incorrect "Username" and "Password".
        2. Verify result.
        """
        # 1. Sign In with incorrect "Username" and "Password".
        start_page.sign_in(username='efg@#', password='123qweasdzcz!@')

        # 2. Verify result.
        start_page.verify_message(xpath=LoginPageConstants.SIGN_IN_ALERT_XPATH, text=LoginPageConstants.INVALID_SIGN_IN_MESSAGE_TEXT)
        self.log.info("Error message appeared")

    def test_valid_username_and_invalid_password_for_sign_in(self, start_page):
        """
        1. Sign In with correct "Username" and incorrect "Password".
        2. Verify result.
        """
        # 1. Sign In with correct "Username" and incorrect "Password".
        start_page.sign_in(username='123', password='123qwer')

        # 2. Verify result.
        start_page.verify_message(xpath=LoginPageConstants.SIGN_IN_ALERT_XPATH, text=LoginPageConstants.INVALID_SIGN_IN_MESSAGE_TEXT)
        self.log.info("Error message appeared")
