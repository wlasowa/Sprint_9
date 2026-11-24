import allure

import helpers
import urls
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage


class TestSignup:
    @allure.title("Создание аккаунта")
    @allure.description(
        "Проверяем, что после регистрации происходит переход"
        " на страницу авторизации и отображается форма входа"
    )
    def test_create_account(self, driver):
        user = helpers.generate_user_data()
        signup_page = SignupPage(driver)
        signin_page = SigninPage(driver)

        signup_page.click_signup_link()
        signup_page.register(user)

        assert signup_page.get_current_url() == urls.SIGNIN_PAGE
        assert signin_page.is_signin_form_shown()
