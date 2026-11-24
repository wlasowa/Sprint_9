from pathlib import Path

import allure

import data
from pages.recipe_create_page import RecipeCreatePage
from pages.recipes_page import RecipesPage

PHOTO_PATH = Path(__file__).resolve().parents[1] / "assets" / "pic.jpeg"


class TestRecipeCreate:
    @allure.title("Создание рецепта")
    @allure.description(
        "Проверяем, что после создания рецепта отображается карточка"
        " с названием, которое заполняли при создании"
    )
    def test_create_recipe(self, authorized_driver):
        recipe_name = data.RECIPE_NAME
        recipes_page = RecipesPage(authorized_driver)
        create_page = RecipeCreatePage(authorized_driver)

        recipes_page.open_create_recipe()
        create_page.fill_name(recipe_name)
        create_page.fill_ingredient(data.INGREDIENT_NAME, data.INGREDIENT_AMOUNT)
        create_page.fill_cooking_time(data.COOKING_TIME)
        create_page.fill_description(data.RECIPE_DESCRIPTION)
        create_page.upload_photo(PHOTO_PATH)
        create_page.submit()

        assert create_page.get_created_recipe_title() == recipe_name
