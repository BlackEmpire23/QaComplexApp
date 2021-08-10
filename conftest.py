import logging
import random


def pytest_runtest_setup(item):
    item.cls.log = logging.getLogger(item.name)
    item.cls.variety = random.choice(range(100000, 999999))


class BaseTest:
    log = logging.getLogger(__name__)
    variety = random.choice(range(100000, 999999))
