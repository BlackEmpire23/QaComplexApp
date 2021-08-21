from selenium.webdriver.common.by import By

from conftest import BaseTest
from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
from constans.base import BaseConstans
from constans.profile_page import ProfilePage
from helpers.base import BaseHelpers
from helpers.login_page import LoginPageHelpers
from helpers.profile_page import ProfileHelpers


class TestPostsAndChat(BaseTest):

    @pytest.fixture(scope='class')
    def driver(self):
        driver = webdriver.Chrome(executable_path=BaseConstans.DRIVER_PATH)
        yield driver
        driver.close()

    def test_create_new_post(self, driver):
        """
        Pre-condition(released in fixtures):
            1. Finish registration flow and enter to the main page with registered user.

        STR:
            1. Create a new post.
            2. Verify result.

        Post-condition(released in fixtures):
            1. Logout.
        """

        # Helper for fill fields
        base_helper = BaseHelpers(driver)
        login_helper = LoginPageHelpers(driver)
        # Finish registration flow and enter to the main page with registered user.
        username, email, password = base_helper.user_data()
        login_helper.registration(username=username,
                                  email=email,
                                  password=password)
        profile_helper = ProfileHelpers(driver)
        # 1. Create a new post.
        profile_helper.create_new_post(title='Hello', body='Test!')
        # 2. Verify result.
        base_helper.verify_message(xpath=ProfilePage.POST_SUCCESS_MESSAGE_XPATH, text=ProfilePage.POST_SUCCESS_MESSAGE_TEXT)
        self.log.info('Saving a post.')
        # Logout.
        profile_helper.logout()

    def test_editing_post(self, driver):
        """
        Pre-condition(released in fixtures):
            1. Finish registration flow and enter to the main page with registered user.
        STR:
            1. Create a new post.
            2. Edit created post.
            3. Verify changes
        Post-condition(released in fixtures):
            1. Logout.
        """
        # Helper for fill fields
        base_helper = BaseHelpers(driver)
        login_helper = LoginPageHelpers(driver)
        profile_helper = ProfileHelpers(driver)
        # Finish registration flow and enter to the main page with registered user.
        username, email, password = base_helper.user_data()
        login_helper.registration(username=username,
                                  email=email,
                                  password=password)
        # 1. Create a new post.
        profile_helper.create_new_post(title='Hell', body='Test!')
        # 2. Edit created post.
        # Click "Edit" button
        base_helper.wait_and_click(locator_type=By.XPATH, locator=ProfilePage.POST_EDIT_BUTTON_XPATH)
        # Change "Title" and change "Body Context"
        base_helper.wait_and_click(locator_type=By.XPATH, locator=ProfilePage.POST_TITLE_XPATH)
        base_helper.wait_until_element_find(locator_type=By.XPATH, locator=ProfilePage.POST_TITLE_XPATH).send_keys('o')
        base_helper.wait_until_element_find(locator_type=By.XPATH, locator=ProfilePage.POST_BODY_CONTENT_XPATH).send_keys(' Text was edit!')
        # Press "Save" button
        base_helper.wait_and_click(locator_type=By.XPATH, locator=ProfilePage.POST_SAVE_BUTTON_XPATH)
        # 3. Verify changes
        base_helper.verify_message(xpath=ProfilePage.POST_SUCCESS_MESSAGE_XPATH, text=ProfilePage.POST_SUCCESSFULLY_UPDATED_TEXT)
        self.log.info('Post was edited.')
        # Logout.
        profile_helper.logout()

    def test_delete_a_new_post(self, driver):
        """
        Pre-conditions(released in fixtures):
            1. Go to https://qa-complex-app-for-testing.herokuapp.com/
            2. Sign In to the resource.
        STR:
            1. Create a new post.
            2. Delete created post.
            3. Verify changes.
        Post-condition(released in fixtures):
            1. Logout.
        """
        # Helper for fill fields
        base_helper = BaseHelpers(driver)
        profile_helper = ProfileHelpers(driver)
        login_helper = LoginPageHelpers(driver)
        # Finish registration flow and enter to the main page with registered user.
        username, email, password = base_helper.user_data()
        login_helper.registration(username=username,
                                  email=email,
                                  password=password)
        # 1. Create a new post.
        profile_helper.create_new_post(title='Hello', body='Test!')
        # 2. Delete created post.
        base_helper.wait_and_click(locator_type=By.XPATH, locator=ProfilePage.POST_DELETE_BUTTON_XPATH)
        self.log.info('Post was deleted.')
        # 3. Verify changes.
        base_helper.verify_message(xpath=ProfilePage.POST_SUCCESS_MESSAGE_XPATH, text=ProfilePage.POST_SUCCESSFULLY_DELETED_TEXT)
        self.log.info('Verify delete message.')
        # Logout.
        profile_helper.logout()

    def test_send_message_to_chat(self, driver):
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
        profile_helper = ProfileHelpers(driver)
        login_helper = LoginPageHelpers(driver)
        # Finish registration flow and enter to the main page with registered user.
        username, email, password = base_helper.user_data()
        login_helper.registration(username=username,
                                  email=email,
                                  password=password)
        # 1. Open chat.
        base_helper.wait_and_click(locator_type=By.XPATH, locator=ProfilePage.CHAT_BUTTON_XPATH)
        self.log.info('Chat is opened.')
        # 2. Send some text to the chat.
        base_helper.wait_until_element_find(locator_type=By.XPATH, locator=ProfilePage.CHAT_TEXT_INPUT_XPATH).send_keys("Hello")
        base_helper.wait_until_element_find(locator_type=By.XPATH, locator=ProfilePage.CHAT_TEXT_INPUT_XPATH).send_keys(Keys.ENTER)
        self.log.info('Message is send.')
        # 3. Verify message
        base_helper.verify_message(xpath=ProfilePage.CHAT_VERIFY_MESSAGE_XPATH, text="Hello")
        self.log.info('Message verified.')
        # Logout.
        profile_helper.logout()
