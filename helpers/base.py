import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class BaseHelpers:
    """ Store base helpers for Web Testing"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=5)

    def wait_until_element_find(self, locator_type, locator):
        """ Wait until element find and return it """
        self.wait.until(EC.presence_of_element_located((locator_type, locator)))
        return self.driver.find_element(by=locator_type, value=locator)

    def wait_and_click(self, locator_type, locator):
        """Wait until element clickable and click"""
        self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
        self.driver.find_element(by=locator_type, value=locator).click()

    def fill_input_field(self, by, locator, value=''):
        """ Find required element using by.X model, clear input field and enter the value """
        field = self.wait_until_element_find(locator_type=by, locator=locator)
        field.clear()
        field.send_keys(value)

    def find_by_contains_text(self, text, element_tag="*"):
        """ Find element using XPATH contains function by text """
        return self.wait_until_element_find(locator_type=By.XPATH, locator=f".//{element_tag}[contains(text(), '{text}')]")

    def verify_message(self, xpath, text):
        """ Verification by text """
        assert self.wait_until_element_find(locator_type=By.XPATH, locator=xpath).text == text

    def user_data(self):
        """ Valid data for user credentials """
        username_text = ''
        for i in range(random.randint(4, 6)):
            username_text += random.choice(string.ascii_letters)
        email_text = ''
        for i in range(random.randint(5, 20)):
            email_text += random.choice(string.ascii_letters).lower()
        password_text = ''
        for i in range(random.randint(4, 13)):
            password_text += random.choice(string.ascii_letters)
            password_text += random.choice(string.punctuation)
            password_text += str(random.randint(1, 9))
        return username_text, email_text, password_text
