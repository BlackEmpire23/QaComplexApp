import logging
import random
import string


def pytest_runtest_setup(item):
    item.cls.log = logging.getLogger(item.name)
    item.cls.variety = random.choice(range(100000, 999999))


class BaseTest:
    log = logging.getLogger(__name__)
    variety = random.choice(range(100000, 999999))
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
