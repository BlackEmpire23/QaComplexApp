import random
import string
from time import sleep

from conftest import BaseTest
from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
from constans.base import BaseConstans
from constans.login_page import LoginPageConstants
from constans.profile_page import ProfilePage


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

        # Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # 2. Type to field 1 or 2 symbols(letters or numbers).
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH).clear()
        text_2_chars = random.choice(string.ascii_letters) + str(random.randint(1, 9))
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH).send_keys(text_2_chars)
        sleep(2)
        # Check alert text
        assert driver.find_element_by_xpath(
            LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_USERNAME_3_CHARS_TEXT
        self.log.info('Alert "Username must be at least 3 characters." appeared.')

        # 3. Clear this field and type 3 or more symbols with special symbol(for ex: @$%_ ^&*).
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH).clear()
        text_with_chars_and_symbol = ''
        for i in range(3):
            text_with_chars_and_symbol += random.choice(string.ascii_letters)
            text_with_chars_and_symbol += random.choice(string.punctuation)
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH).send_keys(text_with_chars_and_symbol)
        sleep(2)
        # Check alert text
        assert driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_ALERT_XPATH).text == \
               LoginPageConstants.ALERT_USERNAME_ONLY_LET_AND_DIG_TEXT
        self.log.info('Alert "Username can only contain letters and numbers." appeared.')

        # 4. Clear this field and type name which is already exists(for ex: 123).
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH).send_keys('123')
        sleep(2)
        # Check alert text
        assert driver.find_element_by_xpath(
            LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_USERNAME_ALREADY_TAKEN_TEXT
        self.log.info('Alert "That username is already taken." appeared.')

        # 5. Clear this field and type more than 30 symbols(letters or numbers)."""
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH).clear()
        text_30_chars = ''
        for i in range(16):
            text_30_chars += random.choice(string.ascii_letters)
            text_30_chars += str(random.randint(1, 9))
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH).send_keys(text_30_chars)
        sleep(2)
        # Check alert text
        assert driver.find_element_by_xpath(
            LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_USERNAME_MAX_LENGTH_TEXT
        self.log.info('Alert "Username cannot exceed 30 characters." appeared')

        # 6. Clear this field, type some text then clear this field
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH).send_keys('ab')
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH).clear()
        sleep(2)
        # Check alert text
        assert driver.find_element_by_xpath(
            LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_USERNAME_3_CHARS_TEXT
        self.log.info('Alert "Username must be at least 3 characters." appeared ')

    def test_email_on_registration_field(self, driver):

        """
        Validation for field "Email".
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Type to field invalid email (for ex:email without '@mail.com') - try different combinations. """

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # Type to field invalid email (for ex: email without "@mail.com") - try different combinations.
        # 'Email' without @mail.com
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH).send_keys('ergqerg')
        sleep(2)
        # Check alert text
        assert driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_EMAIL_VALID_EMAIL_TEXT
        self.log.info('Alert for invalid email appeared')

        # 'Email' without mail.com
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH).send_keys('asd@')
        sleep(2)
        # Check alert text
        assert driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_EMAIL_VALID_EMAIL_TEXT
        self.log.info('Alert for invalid email appeared')

        # Empty 'Email' after fill email
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH).send_keys('asd@gmail')
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH).clear()
        sleep(2)
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

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # 2. Type to field "Password" from 1 to 11 any symbols.
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH).clear()
        password_text = ''
        for i in range(random.randint(1, 11)):
            password_text += random.choice(string.ascii_letters)
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH).send_keys(password_text)
        sleep(2)
        # Check alert text
        assert driver.find_element_by_xpath(
            LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_PASSWORD_MIN_LENGTH_TEXT
        self.log.info('Alert "Password must be at least 12 characters." appeared')

        # 3. Type to field "Password" more than 50 any symbols.
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH).clear()
        password_text = ''
        for i in range(random.randint(50, 100)):
            password_text += random.choice(string.ascii_letters)
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH).send_keys(password_text)
        sleep(2)
        # Check alert text
        assert driver.find_element_by_xpath(
            LoginPageConstants.SIGN_UP_ALERT_XPATH).text == LoginPageConstants.ALERT_PASSWORD_MAX_LENGTH_TEXT
        self.log.info('Alert "Password cannot exceed 50 characters" appeared')

        # 4. Type to field "Password" any text then clear this field
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH).send_keys('123')
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH).clear()
        sleep(2)
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

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # 2. Type to field "Username" (on registration form) some user name (more than 2 characters and less than 30,
        # use letters or numbers only), and make sure that this user name is not using.
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH).send_keys(self.user_name_text)
        self.log.info(f'Type login: "{self.user_name_text}"')

        # 3. Fill the "Email" field with correct email(for ex: example@mail.com), and make sure that email is not using.
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH).send_keys(self.email_text + '@gmail.com')
        self.log.info(f'Type email: "{self.email_text + "@gmail.com"}"')

        # 4. Fill the "Password" field correctly(any symbols, length of password should be between 12 and 50 characters).
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH).send_keys(self.password_text)
        self.log.info(f'Type password: "{self.password_text}"')

        # 5. Press on "Sign up for OurApp" button.
        sleep(2)
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

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # 2. Type to field username (in 'signin' form) correct username
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_USERNAME_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_USERNAME_XPATH).send_keys(
            self.user_name_text)
        self.log.info(f'Type login: "{self.user_name_text}"')

        # 3. Type to field password (in 'signin' form) correct password
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_PASSWORD_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_PASSWORD_XPATH).send_keys(
            self.password_text)
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

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # 2. Fill "Username" field with correct data.
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_USERNAME_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_USERNAME_XPATH).send_keys('123')
        self.log.info('Type login: "123"')

        # 3. Keep field "Password" empty and press "Sign In" button.
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_PASSWORD_XPATH).clear()
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

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # 2. Fill "Username" field with incorrect data.
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_USERNAME_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_USERNAME_XPATH).send_keys('efg@#')
        self.log.info('Type login: "efg@#"')

        # 3. Fill "Password" field with incorrect data.
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_PASSWORD_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_PASSWORD_XPATH).send_keys(
            '123qweasdzcz!@')
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

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get(BaseConstans.START_PAGE_URL)
        self.log.info('Entering to the page')

        # 2. Fill "Username" field with correct data.
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_USERNAME_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_USERNAME_XPATH).send_keys('123')
        self.log.info('Type login: "123"')

        # 3. Fill "Password" field with incorrect data.
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_PASSWORD_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_PASSWORD_XPATH).send_keys('123qwe')
        self.log.info('Type password: "123qwe"')

        # 4. Press "Sign In" button.
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_BUTTON_XPATH).click()
        # Check alert message
        assert driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_ALERT_XPATH).text == LoginPageConstants.INVALID_SIGN_IN_MESSAGE_TEXT
        self.log.info("Error message appeared")
