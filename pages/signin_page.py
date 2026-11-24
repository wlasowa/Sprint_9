import allure
from selenium.webdriver.support import expected_conditions as ec

import urls
from locators import signin_page_locators as loc
from pages.base_page import BasePage


class SigninPage(BasePage):
    @allure.step("Открыть страницу авторизации")
    def open(self):
        self.open_page(urls.SIGNIN_PAGE)

    @allure.step("Ввести логин {username}")
    def fill_username(self, username):
        self.wait_visible(loc.EMAIL_INPUT).send_keys(username)

    @allure.step("Ввести пароль")
    def fill_password(self, password):
        self.wait_visible(loc.PASSWORD_INPUT).send_keys(password)

    @allure.step("Кликнуть «Войти»")
    def click_submit(self):
        self.wait_clickable(loc.LOGIN_BUTTON).click()

    @allure.step("Авторизоваться под логином {username}")
    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_submit()
        self.wait_for(ec.url_to_be(urls.RECIPES_PAGE))

    @allure.step("Проверить, что отображается форма авторизации")
    def is_signin_form_shown(self):
        return self.is_visible(loc.TITLE) and self.is_visible(loc.LOGIN_BUTTON)
