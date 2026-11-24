from selenium.webdriver.common.by import By

RECIPES_TITLE = (By.XPATH, "//h1[text()='Рецепты']")

CREATE_TITLE = (By.XPATH, "//h1[text()='Создание рецепта']")

NAME_INPUT = (By.XPATH, "//div[text()='Название рецепта']/following-sibling::input")
INGREDIENT_INPUT = (By.XPATH, "//div[text()='Ингредиенты']/following-sibling::input")
INGREDIENT_AMOUNT_INPUT = (By.XPATH, "//label[not(.//div)]/input")
INGREDIENT_DROPDOWN_ITEM = (By.XPATH, "//div[text()='{}']")
ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[text()='Добавить ингредиент']")
COOKING_TIME_INPUT = (
    By.XPATH,
    "//div[text()='Время приготовления']/following-sibling::input",
)
DESCRIPTION_TEXTAREA = (
    By.XPATH,
    "//div[text()='Описание рецепта']/following-sibling::textarea",
)
FILE_INPUT = (By.XPATH, "//input[@type='file']")
CREATE_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")

SINGLE_CARD_TITLE = (By.XPATH, "//h1")
