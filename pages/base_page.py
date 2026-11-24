import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from locators import header_locators as header_loc


class BasePage:
    TIMEOUT = 20

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def format_locator(locator, *args):
        by, value = locator
        return by, value.format(*args)

    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.element_to_be_clickable(locator)
        )

    def wait_visible(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.visibility_of_element_located(locator)
        )

    def wait_for(self, condition):
        return WebDriverWait(self.driver, self.TIMEOUT).until(condition)

    def is_visible(self, locator):
        try:
            self.wait_visible(locator)
            return True
        except TimeoutException:
            return False

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Загрузить файл {file_path}")
    def upload_file(self, locator, file_path: str):
        self.find_element(locator).send_keys(file_path)

    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Открыть страницу {url}")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Кликнуть «Войти» в шапке")
    def click_signin_link(self):
        self.wait_clickable(header_loc.SIGNIN_LINK).click()

    @allure.step("Кликнуть «Создать аккаунт» в шапке")
    def click_signup_link(self):
        self.wait_clickable(header_loc.SIGNUP_LINK).click()

    @allure.step("Кликнуть «Создать рецепт» в шапке")
    def click_create_recipe_link(self):
        self.wait_clickable(header_loc.CREATE_RECIPE_LINK).click()

    @allure.step("Проверить, что пользователь авторизован")
    def is_logged_in(self):
        return self.is_visible(header_loc.LOGOUT_LINK)
