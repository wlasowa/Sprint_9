import allure

import urls
from pages.signin_page import SigninPage


class TestSignin:
    @allure.title("Авторизация")
    @allure.description(
        "Проверяем, что после входа происходит переход на главную страницу"
        " и отображается кнопка «Выход»"
    )
    def test_login(self, driver, registered_user):
        signin_page = SigninPage(driver)

        signin_page.login(registered_user["username"], registered_user["password"])

        assert signin_page.get_current_url() == urls.RECIPES_PAGE
        assert signin_page.is_logged_in()
