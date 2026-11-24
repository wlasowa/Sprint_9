import allure
from selenium.webdriver.support import expected_conditions as ec

import urls
from pages.base_page import BasePage


class RecipesPage(BasePage):
    @allure.step("Перейти на страницу создания рецепта")
    def open_create_recipe(self):
        self.click_create_recipe_link()
        self.wait_for(ec.url_to_be(urls.RECIPE_CREATE_PAGE))
