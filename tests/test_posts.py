"""Store tests related to profile page"""
from selenium.webdriver.common.by import By

from conftest import BaseTest
from constans.post_page import PostConstants
from helpers.base import BaseHelpers


class TestPosts(BaseTest):

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
        title = 'Hello'
        post_page = profile_page.click_create_post()
        post_page.create_new_post(title=title, body='Test!')
        self.log.info('Saving a post.')

        # 2. Verify result.
        profile_page.verify_message(xpath=PostConstants.POST_SUCCESS_MESSAGE_XPATH, text=PostConstants.POST_SUCCESS_MESSAGE_TEXT)
        post_page.verify_post(username=username.lower(), title=title)

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
        first_title = 'Hell'
        first_body = 'Test!'
        post_page = profile_page.click_create_post()
        post_page.create_new_post(title=first_title, body=first_body)

        # 2. Edit created post.
        # Click "Edit" button
        post_page.wait_and_click(locator_type=By.XPATH, locator=PostConstants.POST_EDIT_BUTTON_XPATH)

        # Change "Title" and change "Body Context"
        post_page.wait_and_click(locator_type=By.XPATH, locator=PostConstants.POST_TITLE_XPATH)

        # Send_keys - because fields are not empty
        second_title = 'o'
        second_body = ' Text was edit!'
        post_page.wait_until_element_find(locator_type=By.XPATH, locator=PostConstants.POST_TITLE_XPATH).send_keys(second_title)
        post_page.wait_until_element_find(locator_type=By.XPATH, locator=PostConstants.POST_BODY_CONTENT_XPATH).send_keys(second_body)

        # Press "Save" button
        post_page.wait_and_click(locator_type=By.XPATH, locator=PostConstants.POST_SAVE_BUTTON_XPATH)

        # 3. Verify changes
        post_page.verify_message(xpath=PostConstants.POST_SUCCESS_MESSAGE_XPATH, text=PostConstants.POST_SUCCESSFULLY_UPDATED_TEXT)
        post_page.verify_post(username=username.lower(), title=first_title + second_title)
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
        post_page = profile_page.click_create_post()
        post_page.create_new_post(title='Hello', body='Test!')

        # 2. Delete created post.
        post_page.wait_and_click(locator_type=By.XPATH, locator=PostConstants.POST_DELETE_BUTTON_XPATH)
        self.log.info('Post was deleted.')

        # 3. Verify changes.
        post_page.verify_message(xpath=PostConstants.POST_SUCCESS_MESSAGE_XPATH, text=PostConstants.POST_SUCCESSFULLY_DELETED_TEXT)
        self.log.info('Verify delete message.')

    def test_post_search(self, start_page, logout):
        """
        Pre-conditions(released in fixtures):
            1. Go to https://qa-complex-app-for-testing.herokuapp.com/
            2. Sign In to the resource.
        STR:
            1. Create a new post.
            2. Go to search panel and search created message.
            3. Verify result.
        Post-condition(released in fixtures):
            1. Logout.
        """
        # Finish registration flow and enter to the main page with registered user.
        username, email, password = BaseHelpers.user_data(start_page)
        profile_page = start_page.registration(username=username, email=email, password=password)

        # 1. Create a new post.
        post_page = profile_page.click_create_post()
        post_page.create_new_post(title=username, body=username)

        # 2. Go to search panel and search created message.
        profile_page.find_post_by_search_field(username=username)

        # 3. Verify result.
        profile_page.verify_search(username=username)
