import random
import string


class BaseHelpers:
    """ Store base helpers for Web Testing"""

    def __init__(self, driver):
        self.driver = driver

    def fill_input_field(self, by, locator, value=''):
        """Find required element using by.X model, clear input field and enter the value"""
        username = self.driver.find_element(by=by, value=locator)
        username.clear()
        username.send_keys(value)

    def find_by_contains_text(self, text, element_tag="*"):
        """Find element using XPATH contains function by text"""
        return self.driver.find_element_by_xpath(f".//{element_tag}[contains(text(), '{text}')]")

    def credentials(self):
        user_name_text = ''
        for i in range(random.randint(4, 6)):
            user_name_text += random.choice(string.ascii_letters)
        email_text = ''
        for i in range(random.randint(5, 20)):
            email_text += random.choice(string.ascii_letters).lower()
        password_text = ''
        for i in range(random.randint(4, 13)):
            password_text += random.choice(string.ascii_letters)
            password_text += random.choice(string.punctuation)
            password_text += str(random.randint(1, 9))
        return user_name_text, email_text, password_text
