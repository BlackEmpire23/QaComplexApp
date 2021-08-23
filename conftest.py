import logging
import random

import pytest
from selenium import webdriver

from constans.base import BaseConstans
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


def pytest_runtest_setup(item):
    item.cls.log = logging.getLogger(item.name)
    item.cls.variety = random.choice(range(100000, 999999))


class BaseTest:
    log = logging.getLogger(__name__)
    variety = random.choice(range(100000, 999999))
    user_name_text = ''


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome(executable_path=BaseConstans.DRIVER_PATH)
    yield driver
    driver.close()


@pytest.fixture(scope="function")
def start_page(driver):
    driver.get(BaseConstans.START_PAGE_URL)
    return LoginPage(driver)


@pytest.fixture(scope="function")
def logout(driver):
    yield
    ProfilePage(driver).logout()
