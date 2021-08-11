import random
import string
from time import sleep

from conftest import BaseTest
from selenium import webdriver
import pytest


class TestValidationForRegistrationFields(BaseTest):

    @pytest.fixture(scope='class')
    def driver(self):
        driver = webdriver.Chrome(executable_path=r'A:\Python\QaComplexApp\drivers\chromedriver.exe')
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
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info('Entering to the page')

        # 2. Type to field 1 or 2 symbols(letters or numbers).
        username = driver.find_element_by_xpath('.//input[@id="username-register"]')
        username.clear()
        text_2_chars = random.choice(string.ascii_letters) + str(random.randint(1, 9))
        username.send_keys(text_2_chars)
        sleep(5)
        alert = driver.find_element_by_xpath('.//*[contains(text(),"Username must be at least 3 characters.")]')
        assert alert.text == 'Username must be at least 3 characters.'
        self.log.info('Alert "Username must be at least 3 characters." appeared.')

        # 3. Clear this field and type 3 or more symbols with special symbol(for ex: @$%_ ^&*).
        username = driver.find_element_by_xpath('.//input[@id="username-register"]')
        username.clear()
        text_with_chars_and_symbol = ''
        for i in range(3):
            text_with_chars_and_symbol += random.choice(string.ascii_letters)
            text_with_chars_and_symbol += random.choice(string.punctuation)
        username.send_keys(text_with_chars_and_symbol)
        sleep(5)
        alert = driver.find_element_by_xpath('.//*[contains(text(),"Username can only contain letters and numbers.")]')
        assert alert.text == 'Username can only contain letters and numbers.'
        self.log.info('Alert "Username can only contain letters and numbers." appeared.')

        # 4. Clear this field and type name which is already exists(for ex: 123).
        username = driver.find_element_by_xpath('.//input[@id="username-register"]')
        username.clear()
        username.send_keys('123')
        sleep(5)
        alert = driver.find_element_by_xpath('.//*[contains(text(),"That username is already taken.")]')
        assert alert.text == 'That username is already taken.'
        self.log.info('Alert "That username is already taken." appeared.')

        # 5. Clear this field and type more than 30 symbols(letters or numbers)."""
        username = driver.find_element_by_xpath('.//input[@id="username-register"]')
        username.clear()
        text_30_chars = ''
        for i in range(16):
            text_30_chars += random.choice(string.ascii_letters)
            text_30_chars += str(random.randint(1, 9))
        username.send_keys(text_30_chars)
        sleep(5)
        alert = driver.find_element_by_xpath('.//*[contains(text(),"Username cannot exceed 30 characters.")]')
        assert alert.text == 'Username cannot exceed 30 characters.'
        self.log.info('Alert "Username cannot exceed 30 characters." appeared')

        # 6. Clear this field, type some text then clear this field
        username = driver.find_element_by_xpath('.//input[@id="username-register"]')
        username.clear()
        username.send_keys('ab')
        username.clear()
        sleep(5)
        alert = driver.find_element_by_xpath('.//*[contains(text(),"Username must be at least 3 characters.")]')
        assert alert.text == 'Username must be at least 3 characters.'
        self.log.info('Alert "Username must be at least 3 characters." appeared ')

    def test_email_on_registration_field(self, driver):

        """
        Validation for field "Email".
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Type to field invalid email (for ex:email without '@mail.com') - try different combinations. """

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info('Entering to the page')

        # Type to field invalid email (for ex: email without "@mail.com") - try different combinations.
        # 'Email' without @mail.com
        email = driver.find_element_by_xpath('.//input[@name="email"]')
        email.clear()
        email.send_keys('ergqerg')
        sleep(3)
        alert = driver.find_element_by_xpath('.//*[contains(text(),"You must provide a valid email address.")]')
        assert alert.text == 'You must provide a valid email address.'
        self.log.info('Alert for invalid email appeared')
        # 'Email' without mail.com
        email = driver.find_element_by_xpath('.//input[@name="email"]')
        email.clear()
        email.send_keys('asd@')
        sleep(5)
        alert = driver.find_element_by_xpath('.//*[contains(text(),"You must provide a valid email address.")]')
        assert alert.text == 'You must provide a valid email address.'
        self.log.info('Alert for invalid email appeared')
        # Empty 'Email' after fill email
        email = driver.find_element_by_xpath('.//input[@name="email"]')
        email.clear()
        email.send_keys('asd@gmail')
        email.clear()
        sleep(3)
        alert = driver.find_element_by_xpath('.//*[contains(text(),"You must provide a valid email address.")]')
        assert alert.text == 'You must provide a valid email address.'
        self.log.info('Alert for invalid email appeared')

    def test_password_for_registration_form(self, driver):

        """
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Type to field "Password" from 1 to 11 any symbols.
        3. Type to field "Password" more than 50 any symbols.
        4. Type to field "Password" any text then clear this field
        """

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info('Entering to the page')

        # 2. Type to field "Password" from 1 to 11 any symbols.
        password = driver.find_element_by_xpath('.//input[@name="password" and @id="password-register"]')
        password.clear()
        password_text = ''
        for i in range(random.randint(1, 11)):
            password_text += random.choice(string.ascii_letters)
        password.send_keys(password_text)
        sleep(3)
        alert = driver.find_element_by_xpath('.//*[contains(text(),"Password must be at least 12 characters.")]')
        assert alert.text == "Password must be at least 12 characters."
        self.log.info('Alert "Password must be at least 12 characters." appeared')

        # 3. Type to field "Password" more than 50 any symbols.
        password = driver.find_element_by_xpath('.//input[@name="password" and @id="password-register"]')
        password.clear()
        password_text = ''
        for i in range(random.randint(50, 100)):
            password_text += random.choice(string.ascii_letters)
        password.send_keys(password_text)
        sleep(3)
        alert = driver.find_element_by_xpath('.//*[contains(text(),"Password cannot exceed 50 characters")]')
        assert alert.text == "Password cannot exceed 50 characters"
        self.log.info('Alert "Password cannot exceed 50 characters" appeared')

        # 4. Type to field "Password" any text then clear this field
        password = driver.find_element_by_xpath('.//input[@name="password" and @id="password-register"]')
        password.clear()
        password.send_keys('123')
        password.clear()
        sleep(3)
        alert = driver.find_element_by_xpath('.//*[contains(text(),"Password must be at least 12 characters.")]')
        assert alert.text == "Password must be at least 12 characters."
        self.log.info('Alert "Password must be at least 12 characters." appeared')


class TestSuccessfulRegistrationAndSignIn(BaseTest):

    @pytest.fixture(scope='function')
    def driver(self):
        driver = webdriver.Chrome(executable_path=r'A:\Python\QaComplexApp\drivers\chromedriver.exe')
        yield driver
        driver.close()

    @pytest.fixture(scope='class')
    def username_text(self):
        user_name_text = ''
        for i in range(random.randint(6, 15)):
            user_name_text += random.choice(string.ascii_letters)
        return user_name_text

    @pytest.fixture(scope='class')
    def email_text(self):
        email_text = ''
        for i in range(random.randint(5, 15)):
            email_text += random.choice(string.ascii_letters).lower()
        return email_text

    @pytest.fixture(scope='class')
    def password_text(self):
        password_text = ''
        for i in range(random.randint(4, 13)):
            password_text += random.choice(string.ascii_letters)
            password_text += random.choice(string.punctuation)
            password_text += str(random.randint(1, 9))
        return password_text

    def test_successful_registration(self, driver, username_text, email_text, password_text):

        """
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Type to field "Username" (on registration form) some user name (more than 2 characters and less than 30,
        use letters or numbers only), and make sure that this user name is not using.
        3. Fill the "Email" field with correct email(for ex: example@mail.com), and make sure that email is not using.
        4. Fill the "Password" field correctly(any symbols, length of password should be between 12 and 50 characters).
        5. Press on "Sign up for OurApp" button.
        """

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info('Entering to the page')

        # 2. Type to field "Username" (on registration form) some user name (more than 2 characters and less than 30,
        # use letters or numbers only), and make sure that this user name is not using.
        username = driver.find_element_by_xpath('.//input[@id="username-register"]')
        username.send_keys(username_text)
        self.log.info(f'Type login: "{username_text}"')

        # 3. Fill the "Email" field with correct email(for ex: example@mail.com), and make sure that email is not using.
        email = driver.find_element_by_xpath('.//input[@name="email"]')
        email.send_keys(email_text + '@gmail.com')
        self.log.info(f'Type email: "{email_text + "@gmail.com"}"')

        # 4. Fill the "Password" field correctly(any symbols, length of password should be between 12 and 50 characters).
        password = driver.find_element_by_xpath('.//input[@name="password" and @id="password-register"]')
        password.send_keys(password_text)
        self.log.info(f'Type password: "{password_text}"')

        # 5. Press on "Sign up for OurApp" button.
        sign_up_button = driver.find_element_by_xpath('.//*[contains(text(),"Sign up for OurApp")]')
        sleep(2)
        sign_up_button.click()
        sleep(2)
        hello_text = driver.find_element_by_xpath('.//div[@class="text-center"]//h2')
        assert hello_text.text == f'Hello {username_text.lower()}, your feed is empty.'
        self.log.info('Checking login string')

    def test_successful_sign_in(self, driver, username_text, password_text):

        """
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Type to field username (in 'signin' form) correct username
        3. Type to field password (in 'signin' form) correct password
        4. Press "Sign In" button
        """

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info('Entering to the page')

        # 2. Type to field username (in 'signin' form) correct username
        username = driver.find_element_by_xpath(".//*[@name='username' and @class='form-control form-control-sm input-dark']")
        username.clear()
        username.send_keys(username_text)
        self.log.info(f'Type login: "{username_text}"')

        # 3. Type to field password (in 'signin' form) correct password
        password = driver.find_element_by_xpath(".//input[@class='form-control form-control-sm input-dark' and @name='password']")
        password.clear()
        password.send_keys(password_text)
        self.log.info(f'Type password: "{password_text}"')

        # 4. Press "Sign In" button
        sign_in_button = driver.find_element_by_xpath(".//button[@class='btn btn-primary btn-sm']")
        sign_in_button.click()
        hello_text = driver.find_element_by_xpath('.//div[@class="text-center"]//h2')
        assert hello_text.text == f'Hello {username_text.lower()}, your feed is empty.'
        self.log.info('Checking login string')


class TestFailedSignIn(BaseTest):

    @pytest.fixture(scope='class')
    def driver(self):
        driver = webdriver.Chrome(executable_path=r'A:\Python\QaComplexApp\drivers\chromedriver.exe')
        yield driver
        driver.close()

    def test_correct_username_and_empty_password_for_sign_in(self, driver):
        """
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Fill "Username" field with correct data.
        3. Keep field "Password" empty and press "Sign In" button.
        """

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info('Entering to the page')

        # 2. Fill "Username" field with correct data.
        username = driver.find_element_by_xpath(".//*[@name='username' and @class='form-control form-control-sm input-dark']")
        username.clear()
        username.send_keys('123')
        self.log.info('Type login: "123"')

        # 3. Keep field "Password" empty and press "Sign In" button.
        password = driver.find_element_by_xpath(".//input[@class='form-control form-control-sm input-dark' and @name='password']")
        password.clear()
        self.log.info("Password is empty")
        sign_in_button = driver.find_element_by_xpath(".//button[@class='btn btn-primary btn-sm']")
        sign_in_button.click()
        sleep(1)
        validation_text = driver.find_element_by_xpath(".//*[contains(text(),'Invalid username / password')]")
        assert validation_text.text == 'Invalid username / password'
        self.log.info("Error message appeared")

    def test_incorrect_username_and_password_for_sign_in(self, driver):
        """
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Fill "Username" field with incorrect data.
        3. Fill "Password" field with incorrect data.
        4. Press "Sign In" button.
        """

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info('Entering to the page')

        # 2. Fill "Username" field with incorrect data.
        username = driver.find_element_by_xpath(".//*[@name='username' and @class='form-control form-control-sm input-dark']")
        username.clear()
        username.send_keys('efg@#')
        self.log.info('Type login: "efg@#"')

        # 3. Fill "Password" field with incorrect data.
        password = driver.find_element_by_xpath(".//input[@class='form-control form-control-sm input-dark' and @name='password']")
        password.clear()
        password.send_keys('123qweasdzcz!@')
        self.log.info('Type password: "123qweasdzcz!@"')

        # 4. Press "Sign In" button.
        sign_in_button = driver.find_element_by_xpath(".//button[@class='btn btn-primary btn-sm']")
        sign_in_button.click()
        validation_text = driver.find_element_by_xpath(".//*[contains(text(),'Invalid username / password')]")
        assert validation_text.text == 'Invalid username / password'
        self.log.info("Error message appeared")

    def test_valid_username_and_invalid_password_for_sign_in(self, driver):
        """
        1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        2. Fill "Username" field with correct data.
        3. Fill "Password" field with incorrect data.
        4. Press "Sign In" button.
        """

        # 1. Go to https://qa-complex-app-for-testing.herokuapp.com/
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info('Entering to the page')

        # 2. Fill "Username" field with correct data.
        username = driver.find_element_by_xpath(".//*[@name='username' and @class='form-control form-control-sm input-dark']")
        username.clear()
        username.send_keys('123')
        self.log.info('Type login: "123"')

        # 3. Fill "Password" field with incorrect data.
        password = driver.find_element_by_xpath(".//input[@class='form-control form-control-sm input-dark' and @name='password']")
        password.clear()
        password.send_keys('123qwe')
        self.log.info('Type password: "123qwe"')

        # 4. Press "Sign In" button.
        sign_in_button = driver.find_element_by_xpath(".//button[@class='btn btn-primary btn-sm']")
        sign_in_button.click()
        validation_text = driver.find_element_by_xpath(".//*[contains(text(),'Invalid username / password')]")
        assert validation_text.text == 'Invalid username / password'
        self.log.info("Error message appeared")


class TestPosts(BaseTest):

    @pytest.fixture(scope='class')
    def driver(self):
        driver = webdriver.Chrome(executable_path=r'A:\Python\QaComplexApp\drivers\chromedriver.exe')
        yield driver
        driver.close()

    # Fixture for registration form
    @pytest.fixture(scope='function')
    def login(self, driver):
        # Go to the start page
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')
        # Fill username field
        driver.find_element_by_xpath('.//input[@id="username-register"]').clear()
        driver.find_element_by_xpath('.//input[@id="username-register"]').send_keys(self.user_name_text)
        # Fill email field
        driver.find_element_by_xpath('.//input[@name="email"]').clear()
        driver.find_element_by_xpath('.//input[@name="email"]').send_keys(self.email_text + '@gmail.com')
        # Fill password field
        driver.find_element_by_xpath('.//input[@name="password" and @id="password-register"]').clear()
        driver.find_element_by_xpath('.//input[@name="password" and @id="password-register"]').send_keys(self.password_text)
        sleep(1)
        # Press register button
        driver.find_element_by_xpath('.//*[contains(text(),"Sign up for OurApp")]').click()

    @pytest.fixture(scope="function")
    def logout(self, driver):
        yield
        driver.find_element_by_xpath(".//button[contains(text(), 'Sign Out')]").click()
        sleep(1)

    # Sign In fixture
    @pytest.fixture(scope="function")
    def sing_in(self, driver):
        # Go to start page
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')
        # Fill username field
        driver.find_element_by_xpath(".//*[@name='username' and @class='form-control form-control-sm input-dark']").clear()
        driver.find_element_by_xpath(".//*[@name='username' and @class='form-control form-control-sm input-dark']").send_keys(
            self.user_name_text)
        # Fill password field
        driver.find_element_by_xpath(".//input[@class='form-control form-control-sm input-dark' and @name='password']").clear()
        driver.find_element_by_xpath(".//input[@class='form-control form-control-sm input-dark' and @name='password']").send_keys(
            self.password_text)
        # Press "Sign In" button
        driver.find_element_by_xpath(".//button[@class='btn btn-primary btn-sm']").click()

    def test_create_new_post(self, driver, login, logout):
        """
        Pre-condition(released in fixtures):
        1. Finish registration flow and enter to the main page with registered user (fixture - login).

        STR:
        1. Click on "Create Post" button
        2. Fill "Title" field with any text.
        3. Fill "Body Content" with any text.
        4. Click on "Save New Post" button.
        """

        # 1. Click on "Create Post" button
        create_post_button = driver.find_element_by_xpath('.//*[@href="/create-post"]')
        create_post_button.click()
        self.log.info('Clicking on "Create Post" button.')

        # 2. Fill "Title" field with any text.
        title = driver.find_element_by_xpath('.//*[@class="form-control form-control-lg form-control-title"]')
        title.clear()
        title.send_keys('Hello')
        self.log.info('Filled "Title".')

        # 3. Fill "Body Content" with any text.
        body_content = driver.find_element_by_xpath('.//*[@class="body-content tall-textarea form-control"]')
        body_content.clear()
        body_content.send_keys('Test message!')
        self.log.info('Filled "Body content".')

        # 4. Click on "Save New Post" button.
        save_new_post_button = driver.find_element_by_xpath('.//*[contains(text(), "Save New Post")]')
        save_new_post_button.click()
        sleep(1)
        success_message = driver.find_element_by_xpath('.//*[contains(text(), "New post successfully created.")]')
        assert success_message.text == 'New post successfully created.'
        self.log.info('Saving a post.')

    def test_editing_post(self, driver, sing_in, logout):
        """
        Pre-condition(released in fixtures):
        1. Finish registration flow and enter to the main page with registered user (fixture - login).

        STR:
        1. Create a new post.
        2. Edit created post.
        3. Verify changes
        """

        # 1. Create a new post.
        driver.find_element_by_xpath('.//*[@href="/create-post"]').click()
        # Fill "Title"
        driver.find_element_by_xpath('.//*[@class="form-control form-control-lg form-control-title"]').clear()
        driver.find_element_by_xpath('.//*[@class="form-control form-control-lg form-control-title"]').send_keys('Hell')
        # Fill "Body Context"
        driver.find_element_by_xpath('.//*[@class="body-content tall-textarea form-control"]').clear()
        driver.find_element_by_xpath('.//*[@class="body-content tall-textarea form-control"]').send_keys('Test message!')
        # Save post
        driver.find_element_by_xpath('.//*[contains(text(), "Save New Post")]').click()
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
            1. Go to start page.
            2. Signin to the resource.
        STR:
            1. Create a new post.
            2. Delete created post.
            3. Verify changes.
        """
        # 1. Create a new post.
        driver.find_element_by_xpath('.//*[@href="/create-post"]').click()
        # Fill "Title"
        driver.find_element_by_xpath('.//*[@class="form-control form-control-lg form-control-title"]').clear()
        driver.find_element_by_xpath('.//*[@class="form-control form-control-lg form-control-title"]').send_keys('Hell')
        # Fill "Body Context"
        driver.find_element_by_xpath('.//*[@class="body-content tall-textarea form-control"]').clear()
        driver.find_element_by_xpath('.//*[@class="body-content tall-textarea form-control"]').send_keys('Test message!')
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
