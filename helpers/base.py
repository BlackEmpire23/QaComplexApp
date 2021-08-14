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
        assert self.driver.find_element_by_xpath(xpath).text == text
