from time import sleep

from selenium.webdriver.common.by import By

from conftest import BaseTest
from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
from constans.base import BaseConstans
from constans.login_page import LoginPageConstants
from constans.profile_page import ProfilePage
from helpers.base import BaseHelpers


class TestPostsAndChat(BaseTest):

    @pytest.fixture(scope='class')
    def driver(self):
        driver = webdriver.Chrome(executable_path=BaseConstans.DRIVER_PATH)
        yield driver
        driver.close()

    # Fixture for registration form
    @pytest.fixture(scope='function')
    def login(self, driver):
        # Go to the start page
        driver.get(BaseConstans.START_PAGE_URL)
        # Helper for fill fields
        base_helper = BaseHelpers(driver)
        # Fill username field
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value=self.user_name_text)
        # Fill email field
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value=self.email_text + '@gmail.com')
        # Fill password field
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value=self.password_text)
        # Press register button
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_BUTTON_XPATH).click()

    # Fixture for logout
    @pytest.fixture(scope="function")
    def logout(self, driver):
        yield
        driver.find_element_by_xpath(ProfilePage.SIGN_OUT_BUTTON_XPATH).click()
        sleep(1)

    # Sign In fixture
    @pytest.fixture(scope="function")
    def sign_in(self, driver):
        # Go to start page
        driver.get(BaseConstans.START_PAGE_URL)
        # Helper for fill fields
        base_helper = BaseHelpers(driver)
        # Fill username field
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_USERNAME_XPATH, value=self.user_name_text)
        # Fill password field
        base_helper.fill_input_field(by=By.XPATH, locator=LoginPageConstants.SIGN_IN_PASSWORD_XPATH, value=self.password_text)
        # Press "Sign In" button
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_BUTTON_XPATH).click()

    def test_create_new_post(self, driver, login, logout):
        """
        Pre-condition(released in fixtures):
            1. Finish registration flow and enter to the main page with registered user (fixture - login).

        STR:
            1. Click on "Create Post" button
            2. Fill "Title" field with any text.
            3. Fill "Body Content" with any text.
            4. Click on "Save New Post" button.

        Post-condition(released in fixtures):
            1. Logout.
        """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)

        # 1. Click on "Create Post" button
        driver.find_element_by_xpath(ProfilePage.CREATE_POST_BUTTON_XPATH).click()
        self.log.info('Clicking on "Create Post" button.')

        # 2. Fill "Title" field with any text.
        base_helper.fill_input_field(by=By.XPATH, locator=ProfilePage.POST_TITLE_XPATH, value='Hello')
        self.log.info('Filled "Title".')

        # 3. Fill "Body Content" with any text.
        base_helper.fill_input_field(by=By.XPATH, locator=ProfilePage.POST_BODY_CONTENT_XPATH, value='Test message!')
        self.log.info('Filled "Body content".')

        # 4. Click on "Save New Post" button.
        driver.find_element_by_xpath(ProfilePage.POST_SAVE_BUTTON_XPATH).click()
        sleep(1)
        base_helper.verify_message(xpath=ProfilePage.POST_SUCCESS_MESSAGE_XPATH, text=ProfilePage.POST_SUCCESS_MESSAGE_TEXT)
        self.log.info('Saving a post.')

    def test_editing_post(self, driver, sign_in, logout):
        """
        Pre-condition(released in fixtures):
            1. Finish registration flow and enter to the main page with registered user (fixture - login).

        STR:
            1. Create a new post.
            2. Edit created post.
            3. Verify changes

        Post-condition(released in fixtures):
            1. Logout.
        """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)

        # 1. Create a new post.
        driver.find_element_by_xpath(ProfilePage.CREATE_POST_BUTTON_XPATH).click()
        # Fill "Title"
        base_helper.fill_input_field(by=By.XPATH, locator=ProfilePage.POST_TITLE_XPATH, value='Hell')
        # Fill "Body Context"
        base_helper.fill_input_field(by=By.XPATH, locator=ProfilePage.POST_BODY_CONTENT_XPATH, value='Test message!')
        # Save post
        driver.find_element_by_xpath(ProfilePage.POST_SAVE_BUTTON_XPATH).click()
        sleep(1)
        self.log.info('Creating a post.')

        # 2. Edit created post.
        # Click "Edit" button
        driver.find_element_by_xpath(ProfilePage.POST_EDIT_BUTTON_XPATH).click()
        # Change "Title"
        driver.find_element_by_xpath(ProfilePage.POST_TITLE_XPATH).send_keys('o')
        # Change "Body Context"
        driver.find_element_by_xpath(ProfilePage.POST_BODY_CONTENT_XPATH).send_keys(' Text was edit!')
        # Press "Save" button
        driver.find_element_by_xpath(ProfilePage.POST_SAVE_BUTTON_XPATH).click()
        sleep(1)

        # 3. Verify changes
        base_helper.verify_message(xpath=ProfilePage.POST_SUCCESS_MESSAGE_XPATH, text=ProfilePage.POST_SUCCESSFULLY_UPDATED_TEXT)
        self.log.info('Post was edited.')

    def test_delete_a_new_post(self, driver, sign_in, logout):
        """
        Pre-conditions(released in fixtures):
            1. Go to https://qa-complex-app-for-testing.herokuapp.com/
            2. Signin to the resource.
        STR:
            1. Create a new post.
            2. Delete created post.
            3. Verify changes.

        Post-condition(released in fixtures):
            1. Logout.
        """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)
        # 1. Create a new post.
        driver.find_element_by_xpath(ProfilePage.CREATE_POST_BUTTON_XPATH).click()
        # Fill "Title"
        base_helper.fill_input_field(by=By.XPATH, locator=ProfilePage.POST_TITLE_XPATH, value='Hell')
        # Fill "Body Context"
        base_helper.fill_input_field(by=By.XPATH, locator=ProfilePage.POST_BODY_CONTENT_XPATH, value='Test message!')
        # Save post
        driver.find_element_by_xpath(ProfilePage.POST_SAVE_BUTTON_XPATH).click()
        sleep(1)
        self.log.info('Creating a post.')

        # 2. Delete created post.
        driver.find_element_by_xpath(ProfilePage.POST_DELETE_BUTTON_XPATH).click()
        self.log.info('Post was deleted.')

        # 3. Verify changes.
        base_helper.verify_message(xpath=ProfilePage.POST_SUCCESS_MESSAGE_XPATH, text=ProfilePage.POST_SUCCESSFULLY_DELETED_TEXT)
        self.log.info('Verify delete message.')

    def test_send_message_to_chat(self, driver, sign_in, logout):
        """
        Pre-conditions(released in fixtures):
            1. Go to https://qa-complex-app-for-testing.herokuapp.com/
            2. Success registration.

        STR:
            1. Open chat.
            2. Send some text to the chat.
            3. Verify message

        Post-condition(released in fixtures):
            1. Logout.
        """
        # Helper for fill fields
        base_helper = BaseHelpers(driver)

        # 1. Open chat.
        driver.find_element_by_xpath(ProfilePage.CHAT_BUTTON_XPATH).click()
        self.log.info('Chat is opened.')

        # 2. Send some text to the chat.
        driver.find_element_by_xpath(ProfilePage.CHAT_TEXT_INPUT_XPATH).send_keys("Hello")
        driver.find_element_by_xpath(ProfilePage.CHAT_TEXT_INPUT_XPATH).send_keys(Keys.ENTER)
        self.log.info('Message is send.')

        # 3. Verify message
        base_helper.verify_message(xpath=ProfilePage.CHAT_VERIFY_MESSAGE_XPATH, text="Hello")
        self.log.info('Message verified.')
