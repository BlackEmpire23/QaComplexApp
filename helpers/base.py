import random
import string
from time import sleep


class BaseHelpers:
    """ Store base helpers for Web Testing"""

    def __init__(self, driver):
        self.driver = driver

    def fill_input_field(self, by, locator, value=''):
        """Find required element using by.X model, clear input field and enter the value"""
        field = self.driver.find_element(by=by, value=locator)
        field.clear()
        field.send_keys(value)
        sleep(1)

    def find_by_contains_text(self, text, element_tag="*"):
        """Find element using XPATH contains function by text"""
        return self.driver.find_element_by_xpath(f".//{element_tag}[contains(text(), '{text}')]")

    def verify_message(self, xpath, text):
        """
        Verification by text
        """
        assert self.driver.find_element_by_xpath(xpath).text == text

    def user_data(self):
        """
        Valid data for user credentials
        """
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
