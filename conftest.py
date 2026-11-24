import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import helpers
import urls
import users
from locators import recipes_locators as recipes_loc
from pages.recipes_page import RecipesPage
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage

SELENOID_URL = os.getenv("SELENOID_URL")


@pytest.fixture
def driver(request):
    options = ChromeOptions()
    options.add_argument("--window-size=1440,1200")
    if SELENOID_URL:
        wd = webdriver.Remote(command_executor=SELENOID_URL, options=options)
    else:
        wd = webdriver.Chrome(options=options)
    wd.get(urls.RECIPES_PAGE)
    WebDriverWait(wd, 20).until(
        ec.visibility_of_element_located(recipes_loc.RECIPES_TITLE)
    )
    yield wd
    wd.quit()


@pytest.fixture
def registered_user(driver):
    user = helpers.generate_user_data()
    recipes_page = RecipesPage(driver)
    recipes_page.click_signup_link()
    signup_page = SignupPage(driver)
    signup_page.register(user)
    return user


@pytest.fixture
def authorized_driver(driver):
    signin_page = SigninPage(driver)
    signin_page.open()
    signin_page.login(users.USER_LOGIN, users.USER_PASSWORD)
    return driver
