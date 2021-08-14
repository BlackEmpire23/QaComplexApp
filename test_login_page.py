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


class TestValidationForRegistrationFields(BaseTest):

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
        assert driver.find_element_by_xpath(
            LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_USERNAME_3_CHARS_TEXT
        self.log.info('Alert "Username must be at least 3 characters." appeared.')

        # 3. Clear this field and type 3 or more symbols with special symbol(for ex: @$%_ ^&*).
        text_with_chars_and_symbol = ''
        for i in range(3):
            text_with_chars_and_symbol += random.choice(string.ascii_letters)
            text_with_chars_and_symbol += random.choice(string.punctuation)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value=text_with_chars_and_symbol)
        sleep(2)
        # Check alert text
        assert driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_ALERT_XPATH).text == \
               LoginPageConstants.ALERT_USERNAME_ONLY_LET_AND_DIG_TEXT
        self.log.info('Alert "Username can only contain letters and numbers." appeared.')

        # 4. Clear this field and type name which is already exists(for ex: 123).
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value='123')
        # Check alert text
        assert driver.find_element_by_xpath(
            LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_USERNAME_ALREADY_TAKEN_TEXT
        self.log.info('Alert "That username is already taken." appeared.')

        # 5. Clear this field and type more than 30 symbols(letters or numbers)."""
        text_30_chars = ''
        for i in range(16):
            text_30_chars += random.choice(string.ascii_letters)
            text_30_chars += str(random.randint(1, 9))
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value=text_30_chars)
        # Check alert text
        assert driver.find_element_by_xpath(
            LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_USERNAME_MAX_LENGTH_TEXT
        self.log.info('Alert "Username cannot exceed 30 characters." appeared')

        # 6. Clear this field, type some text then clear this field
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value='abc')
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        # Check alert text
        assert driver.find_element_by_xpath(
            LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_USERNAME_3_CHARS_TEXT
        self.log.info('Alert "Username must be at least 3 characters." appeared ')

    def test_email_on_registration_field(self, driver):

        """
        Validation for field "Email".
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Type to field invalid email (for ex:email without '@mail.com') - try different combinations. """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # Type to field invalid email (for ex: email without "@mail.com") - try different combinations.
        # 'Email' without @mail.com
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value='ergqerg')

        # Check alert text
        assert driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_EMAIL_VALID_EMAIL_TEXT
        self.log.info('Alert for invalid email appeared')

        # 'Email' without mail.com
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value='asd@')

        # Check alert text
        assert driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_EMAIL_VALID_EMAIL_TEXT
        self.log.info('Alert for invalid email appeared')

        # Empty 'Email' after fill email
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value='asd@')
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH)

        # Check alert text
        assert driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_EMAIL_VALID_EMAIL_TEXT
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
        assert driver.find_element_by_xpath(
            LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_PASSWORD_MIN_LENGTH_TEXT
        self.log.info('Alert "Password must be at least 12 characters." appeared')

        # 3. Type to field "Password" more than 50 any symbols.
        password_text = ''
        for i in range(random.randint(50, 100)):
            password_text += random.choice(string.ascii_letters)
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value=password_text)

        # Check alert text
        assert driver.find_element_by_xpath(
            LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_PASSWORD_MAX_LENGTH_TEXT
        self.log.info('Alert "Password cannot exceed 50 characters" appeared')

        # 4. Type to field "Password" any text then clear this field
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value='123')
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH)

        # Check alert text
        assert driver.find_element_by_xpath(
            LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_PASSWORD_MIN_LENGTH_TEXT
        self.log.info('Alert "Password must be at least 12 characters." appeared')


class TestSuccessfulRegistrationAndSignIn(BaseTest):

    @pytest.fixture(scope='function')
    def driver(self):
        driver = webdriver.Chrome(executable_path=BaseConstans.DRIVER_PATH)
        yield driver
        driver.close()

    def test_successful_registration(self, driver):
        """
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Type to field "Username" (on registration form) some user name (more than 2 characters and less than 30,
        use letters or numbers only), and make sure that this user name is not using.
        3. Fill the "Email" field with correct email(for ex: example@mail.com), and make sure that email is not using.
        4. Fill the "Password" field correctly(any symbols, length of password should be between 12 and 50 characters).
        5. Press on "Sign up for OurApp" button.
        """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # 2. Type to field "Username" (on registration form) some user name (more than 2 characters and less than 30,
        # use letters or numbers only), and make sure that this user name is not using.
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value=self.user_name_text)
        self.log.info(f'Type login: "{self.user_name_text}"')

        # 3. Fill the "Email" field with correct email(for ex: example@mail.com), and make sure that email is not using.
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value=self.email_text + '@gmail.com')
        self.log.info(f'Type email: "{self.email_text + "@gmail.com"}"')

        # 4. Fill the "Password" field correctly(any symbols, length of password should be between 12 and 50 characters).
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value=self.password_text)
        self.log.info(f'Type password: "{self.password_text}"')

        # 5. Press on "Sign up for OurApp" button.
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_BUTTON_XPATH).click()
        sleep(2)
        # Check "Hello" message
        assert driver.find_element_by_xpath(ProfilePage.HELLO_MESSAGE_XPATH).text == ProfilePage.HELLO_MESSAGE_TEXT.format(
            lower_username=self.user_name_text.lower())
        self.log.info('Checking login string')

    def test_successful_sign_in(self, driver):
        """
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Type to field username (in 'signin' form) correct username
        3. Type to field password (in 'signin' form) correct password
        4. Press "Sign In" button
        """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # 2. Type to field username (in 'Sign In' form) correct username
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_USERNAME_XPATH, value=self.user_name_text)
        self.log.info(f'Type login: "{self.user_name_text}"')

        # 3. Type to field password (in 'Sign In' form) correct password
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_PASSWORD_XPATH, value=self.password_text)
        self.log.info(f'Type password: "{self.password_text}"')

        # 4. Press "Sign In" button
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_BUTTON_XPATH).click()
        # Check "Hello" message
        assert driver.find_element_by_xpath(ProfilePage.HELLO_MESSAGE_XPATH).text == ProfilePage.HELLO_MESSAGE_TEXT.format(
            lower_username=self.user_name_text.lower())
        self.log.info('Checking login string')


class TestFailedSignIn(BaseTest):

    @pytest.fixture(scope='class')
    def driver(self):
        driver = webdriver.Chrome(executable_path=BaseConstans.DRIVER_PATH)
        yield driver
        driver.close()

    def test_correct_username_and_empty_password_for_sign_in(self, driver):
        """
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Fill "Username" field with correct data.
        3. Keep field "Password" empty and press "Sign In" button.
        """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # 2. Fill "Username" field with correct data.
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_USERNAME_XPATH, value='123')
        self.log.info('Type login: "123"')

        # 3. Keep field "Password" empty and press "Sign In" button.
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_PASSWORD_XPATH)
        self.log.info("Password is empty")
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_BUTTON_XPATH).click()
        sleep(1)
        # Check alert message
        assert driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_ALERT_XPATH).text == LoginPageConstants.INVALID_SIGN_IN_MESSAGE_TEXT
        self.log.info("Error message appeared")

    def test_incorrect_username_and_password_for_sign_in(self, driver):
        """
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Fill "Username" field with incorrect data.
        3. Fill "Password" field with incorrect data.
        4. Press "Sign In" button.
        """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # 2. Fill "Username" field with incorrect data.
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_USERNAME_XPATH, value='efg@#')
        self.log.info('Type login: "efg@#"')

        # 3. Fill "Password" field with incorrect data.
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_PASSWORD_XPATH, value='123qweasdzcz!@')
        self.log.info('Type password: "123qweasdzcz!@"')

        # 4. Press "Sign In" button.
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_BUTTON_XPATH).click()
        # Check alert message
        assert driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_ALERT_XPATH).text == LoginPageConstants.INVALID_SIGN_IN_MESSAGE_TEXT
        self.log.info("Error message appeared")

    def test_valid_username_and_invalid_password_for_sign_in(self, driver):
        """
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Fill "Username" field with correct data.
        3. Fill "Password" field with incorrect data.
        4. Press "Sign In" button.
        """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # 2. Fill "Username" field with correct data.
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_USERNAME_XPATH, value='123')
        self.log.info('Type login: "123"')

        # 3. Fill "Password" field with incorrect data.
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_PASSWORD_XPATH, value='123qwe')
        self.log.info('Type password: "123qwe"')

        # 4. Press "Sign In" button.
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_BUTTON_XPATH).click()
        # Check alert message
        assert driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_ALERT_XPATH).text == LoginPageConstants.INVALID_SIGN_IN_MESSAGE_TEXT
        self.log.info("Error message appeared")
