import re

import allure

from locators import recipes_locators as loc
from pages.base_page import BasePage


class RecipeCreatePage(BasePage):
    @allure.step("Ввести название рецепта {name}")
    def fill_name(self, name):
        self.wait_visible(loc.NAME_INPUT).send_keys(name)

    @allure.step("Добавить ингредиент «{name}» в количестве {amount}")
    def fill_ingredient(self, name, amount):
        self.wait_visible(loc.INGREDIENT_INPUT).send_keys(name)
        self.wait_clickable(
            self.format_locator(loc.INGREDIENT_DROPDOWN_ITEM, name)
        ).click()
        self.wait_visible(loc.INGREDIENT_AMOUNT_INPUT).send_keys(amount)
        self.wait_clickable(loc.ADD_INGREDIENT_BUTTON).click()

    @allure.step("Ввести время приготовления {minutes} минут")
    def fill_cooking_time(self, minutes):
        self.wait_visible(loc.COOKING_TIME_INPUT).send_keys(minutes)

    @allure.step("Ввести описание рецепта")
    def fill_description(self, text):
        self.wait_visible(loc.DESCRIPTION_TEXTAREA).send_keys(text)

    @allure.step("Загрузить фото рецепта")
    def upload_photo(self, path):
        self.upload_file(loc.FILE_INPUT, str(path))

    @allure.step("Кликнуть «Создать рецепт» и дождаться сохранения")
    def submit(self):
        self.wait_clickable(loc.CREATE_BUTTON).click()
        self.wait_for(lambda d: re.search(r"/recipes/\d+/?$", d.current_url))

    @allure.step("Получить название созданного рецепта")
    def get_created_recipe_title(self):
        return self.wait_visible(loc.SINGLE_CARD_TITLE).text
