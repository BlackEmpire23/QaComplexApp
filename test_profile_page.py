"""Store tests related to profile page"""
from selenium.webdriver.common.by import By

from conftest import BaseTest
from selenium.webdriver.common.keys import Keys
from constans.profile_page import ProfilePageConstants
from helpers.base import BaseHelpers


class TestPostsAndChat(BaseTest):

    def test_create_new_post(self, start_page, logout):
        """
        Pre-condition(released in fixtures):
            1. Finish registration flow and enter to the main page with registered user.

        STR:
            1. Create a new post.
            2. Verify result.

        Post-condition(released in fixtures):
            1. Logout.
        """
        # Finish registration flow and enter to the main page with registered user.
        username, email, password = BaseHelpers.user_data(start_page)
        profile_page = start_page.registration(username=username, email=email, password=password)

        # 1. Create a new post.
        profile_page.create_new_post(title='Hello', body='Test!')

        # 2. Verify result.
        profile_page.verify_message(xpath=ProfilePageConstants.POST_SUCCESS_MESSAGE_XPATH,
                                    text=ProfilePageConstants.POST_SUCCESS_MESSAGE_TEXT)
        self.log.info('Saving a post.')

    def test_editing_post(self, start_page, logout):
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
        # Finish registration flow and enter to the main page with registered user.
        username, email, password = BaseHelpers.user_data(start_page)
        profile_page = start_page.registration(username=username, email=email, password=password)

        # 1. Create a new post.
        profile_page.create_new_post(title='Hell', body='Test!')

        # 2. Edit created post.
        # Click "Edit" button
        profile_page.wait_and_click(locator_type=By.XPATH, locator=ProfilePageConstants.POST_EDIT_BUTTON_XPATH)

        # Change "Title" and change "Body Context"
        profile_page.wait_and_click(locator_type=By.XPATH, locator=ProfilePageConstants.POST_TITLE_XPATH)

        # Send_keys - because fields are not empty
        profile_page.wait_until_element_find(locator_type=By.XPATH, locator=ProfilePageConstants.POST_TITLE_XPATH).send_keys('o')
        profile_page.wait_until_element_find(locator_type=By.XPATH, locator=ProfilePageConstants.POST_BODY_CONTENT_XPATH).send_keys(
            ' Text was edit!')

        # Press "Save" button
        profile_page.wait_and_click(locator_type=By.XPATH, locator=ProfilePageConstants.POST_SAVE_BUTTON_XPATH)

        # 3. Verify changes
        profile_page.verify_message(xpath=ProfilePageConstants.POST_SUCCESS_MESSAGE_XPATH,
                                    text=ProfilePageConstants.POST_SUCCESSFULLY_UPDATED_TEXT)
        self.log.info('Post was edited.')

    def test_delete_a_new_post(self, start_page, logout):
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
        # Finish registration flow and enter to the main page with registered user.
        username, email, password = BaseHelpers.user_data(start_page)
        profile_page = start_page.registration(username=username, email=email, password=password)

        # 1. Create a new post.
        profile_page.create_new_post(title='Hello', body='Test!')

        # 2. Delete created post.
        profile_page.wait_and_click(locator_type=By.XPATH, locator=ProfilePageConstants.POST_DELETE_BUTTON_XPATH)
        self.log.info('Post was deleted.')

        # 3. Verify changes.
        profile_page.verify_message(xpath=ProfilePageConstants.POST_SUCCESS_MESSAGE_XPATH,
                                    text=ProfilePageConstants.POST_SUCCESSFULLY_DELETED_TEXT)
        self.log.info('Verify delete message.')

    def test_send_message_to_chat(self, start_page, logout):
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
        # Finish registration flow and enter to the main page with registered user.
        username, email, password = BaseHelpers.user_data(start_page)
        profile_page = start_page.registration(username=username, email=email, password=password)

        # 1. Open chat.
        profile_page.wait_and_click(locator_type=By.XPATH, locator=ProfilePageConstants.CHAT_BUTTON_XPATH)
        self.log.info('Chat is opened.')

        # 2. Send some text to the chat.
        profile_page.wait_until_element_find(locator_type=By.XPATH, locator=ProfilePageConstants.CHAT_TEXT_INPUT_XPATH).send_keys("Hello")
        profile_page.wait_until_element_find(locator_type=By.XPATH, locator=ProfilePageConstants.CHAT_TEXT_INPUT_XPATH).send_keys(
            Keys.ENTER)
        self.log.info('Message is send.')

        # 3. Verify message
        profile_page.verify_message(xpath=ProfilePageConstants.CHAT_VERIFY_MESSAGE_XPATH, text="Hello")
        self.log.info('Message verified.')
