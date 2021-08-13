from time import sleep

from conftest import BaseTest
from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
from constans.base import BaseConstans
from constans.login_page import LoginPageConstants
from constans.profile_page import ProfilePage
from helpers.base import BaseHelpers


class TestPosts(BaseTest):

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
        # Fill username field
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH).send_keys(self.user_name_text)
        # Fill email field
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH).send_keys(self.email_text + '@gmail.com')
        # Fill password field
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH).send_keys(self.password_text)
        sleep(1)
        # Press register button
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_BUTTON_XPATH).click()

    @pytest.fixture(scope="function")
    def logout(self, driver):
        yield
        driver.find_element_by_xpath(ProfilePage.SIGN_OUT_BUTTON_XPATH).click()
        sleep(1)

    # Sign In fixture
    @pytest.fixture(scope="function")
    def sing_in(self, driver):
        # Go to start page
        driver.get(BaseConstans.START_PAGE_URL)
        # Fill username field
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_USERNAME_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_USERNAME_XPATH).send_keys(
            self.user_name_text)
        # Fill password field
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_PASSWORD_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_IN_PASSWORD_XPATH).send_keys(
            self.password_text)
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

        # 1. Click on "Create Post" button
        driver.find_element_by_xpath(ProfilePage.CREATE_POST_BUTTON_XPATH).click()
        self.log.info('Clicking on "Create Post" button.')

        # 2. Fill "Title" field with any text.
        driver.find_element_by_xpath(ProfilePage.POST_TITLE_XPATH).clear()
        driver.find_element_by_xpath(ProfilePage.POST_TITLE_XPATH).send_keys('Hello')
        self.log.info('Filled "Title".')

        # 3. Fill "Body Content" with any text.
        driver.find_element_by_xpath(ProfilePage.POST_BODY_CONTENT_XPATH).clear()
        driver.find_element_by_xpath(ProfilePage.POST_BODY_CONTENT_XPATH).send_keys('Test message!')
        self.log.info('Filled "Body content".')

        # 4. Click on "Save New Post" button.
        driver.find_element_by_xpath(ProfilePage.POST_SAVE_BUTTON_XPATH).click()
        sleep(1)
        assert driver.find_element_by_xpath(ProfilePage.POST_SUCCESS_MESSAGE_XPATH).text == ProfilePage.POST_SUCCESS_MESSAGE_TEXT
        self.log.info('Saving a post.')

    def test_editing_post(self, driver, sing_in, logout):
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

        # 1. Create a new post.
        driver.find_element_by_xpath(ProfilePage.CREATE_POST_BUTTON_XPATH).click()
        # Fill "Title"
        driver.find_element_by_xpath(ProfilePage.POST_TITLE_XPATH).clear()
        driver.find_element_by_xpath(ProfilePage.POST_TITLE_XPATH).send_keys('Hell')
        # Fill "Body Context"
        driver.find_element_by_xpath(ProfilePage.POST_BODY_CONTENT_XPATH).clear()
        driver.find_element_by_xpath(ProfilePage.POST_BODY_CONTENT_XPATH).send_keys('Test message!')
        # Save post
        driver.find_element_by_xpath(ProfilePage.POST_SAVE_BUTTON_XPATH).click()
        sleep(1)
        self.log.info('Creating a post.')

        # 2. Edit created post.
        # Click "Edit" button
        driver.find_element_by_xpath(".//*[@class='text-primary mr-2']").click()
        # Change "Title"
        driver.find_element_by_xpath('.//*[@value="Hell"]').send_keys('o')
        # Change "Body Context"
        driver.find_element_by_xpath(".//textarea[@id='post-body']").send_keys(' Text was edit!')
        # Press "Save" button
        save_updates_button = driver.find_element_by_xpath('.//*[contains(text(), "Save Updates")]')
        save_updates_button.click()
        sleep(1)

        # 3. Verify changes
        assert driver.find_element_by_xpath('.//*[contains(text(), "Post successfully updated.")]').text == 'Post successfully updated.'
        self.log.info('Post was edited.')

    def test_delete_a_new_post(self, driver, sing_in, logout):
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
        # 1. Create a new post.
        driver.find_element_by_xpath(ProfilePage.CREATE_POST_BUTTON_XPATH).click()
        # Fill "Title"
        driver.find_element_by_xpath(ProfilePage.POST_TITLE_XPATH).clear()
        driver.find_element_by_xpath(ProfilePage.POST_TITLE_XPATH).send_keys('Hell')
        # Fill "Body Context"
        driver.find_element_by_xpath(ProfilePage.POST_BODY_CONTENT_XPATH).clear()
        driver.find_element_by_xpath(ProfilePage.POST_BODY_CONTENT_XPATH).send_keys('Test message!')
        # Save post
        driver.find_element_by_xpath('.//*[contains(text(), "Save New Post")]').click()
        sleep(1)
        self.log.info('Creating a post.')

        # 2. Delete created post.
        driver.find_element_by_xpath('.//*[@class="delete-post-button text-danger"]').click()
        self.log.info('Post was deleted.')

        # 3. Verify changes.
        assert driver.find_element_by_xpath('.//*[contains(text(), "Post successfully deleted")]').text == 'Post successfully deleted'
        self.log.info('Verify delete message.')


class TestChat(BaseTest):

    @pytest.fixture(scope='class')
    def driver(self):
        driver = webdriver.Chrome(executable_path=BaseConstans.DRIVER_PATH)
        yield driver
        driver.close()

    # Fixture for registration form
    @pytest.fixture(scope='function')
    def login(self, driver):
        base_helper = BaseHelpers(driver)
        username_text, email_text, password_text = base_helper.credentials()
        # Go to the start page
        driver.get(BaseConstans.START_PAGE_URL)
        # Fill username field
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH).send_keys(username_text)
        # Fill email field
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH).send_keys(email_text + '@gmail.com')
        # Fill password field
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH).clear()
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH).send_keys(password_text)
        sleep(1)
        # Press register button
        driver.find_element_by_xpath(LoginPageConstants.SIGN_UP_BUTTON_XPATH).click()

    @pytest.fixture(scope="function")
    def logout(self, driver):
        yield
        sleep(0.5)
        driver.find_element_by_xpath(ProfilePage.SIGN_OUT_BUTTON_XPATH).click()
        sleep(1)

    def test_send_message_to_chat(self, driver, login, logout):
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

        # 1. Open chat.
        driver.find_element_by_xpath('.//*[@class="text-white mr-2 header-chat-icon"]').click()
        self.log.info('Chat is opened.')

        # 2. Send some text to the chat.
        driver.find_element_by_xpath('.//input[@id="chatField"]').send_keys("Hello")
        driver.find_element_by_xpath('.//input[@id="chatField"]').send_keys(Keys.ENTER)
        self.log.info('Message is send.')

        # 3. Verify message
        assert driver.find_element_by_xpath('.//*[@class="chat-message-inner"]').text == "Hello"
        self.log.info('Message verified.')
