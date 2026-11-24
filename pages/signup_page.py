import allure
from selenium.webdriver.support import expected_conditions as ec

import urls
from locators import signup_page_locators as loc
from pages.base_page import BasePage


class SignupPage(BasePage):
    @allure.step("Ввести имя {value}")
    def fill_first_name(self, value):
        self.wait_visible(loc.FIRST_NAME_INPUT).send_keys(value)

    @allure.step("Ввести фамилию {value}")
    def fill_last_name(self, value):
        self.wait_visible(loc.LAST_NAME_INPUT).send_keys(value)

    @allure.step("Ввести имя пользователя {value}")
    def fill_username(self, value):
        self.wait_visible(loc.USERNAME_INPUT).send_keys(value)

    @allure.step("Ввести email {value}")
    def fill_email(self, value):
        self.wait_visible(loc.EMAIL_INPUT).send_keys(value)

    @allure.step("Ввести пароль")
    def fill_password(self, value):
        self.wait_visible(loc.PASSWORD_INPUT).send_keys(value)

    @allure.step("Кликнуть «Создать аккаунт»")
    def click_submit(self):
        self.wait_clickable(loc.SUBMIT_BUTTON).click()

    @allure.step("Зарегистрировать пользователя")
    def register(self, user):
        self.fill_first_name(user["first_name"])
        self.fill_last_name(user["last_name"])
        self.fill_username(user["username"])
        self.fill_email(user["email"])
        self.fill_password(user["password"])
        self.click_submit()
        self.wait_for(ec.url_to_be(urls.SIGNIN_PAGE))
