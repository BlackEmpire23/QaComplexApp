from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from conftest import BaseTest
from constans.chat import ChatConstants
from constans.profile_page import ProfilePageConstants
from helpers.base import BaseHelpers


class TestChat(BaseTest):

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
        text = "Hello!"
        profile_page.wait_until_element_find(locator_type=By.XPATH, locator=ChatConstants.CHAT_TEXT_INPUT_XPATH).send_keys(text)
        profile_page.wait_until_element_find(locator_type=By.XPATH, locator=ChatConstants.CHAT_TEXT_INPUT_XPATH).send_keys(
            Keys.ENTER)
        self.log.info('Message is send.')

        # 3. Verify message
        profile_page.verify_message(xpath=ChatConstants.CHAT_VERIFY_MESSAGE_XPATH, text=text)
        self.log.info('Message verified.')
