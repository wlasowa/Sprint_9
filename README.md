# Sprint_9

UI-автотесты для сервиса Foodgram (продуктовый помощник): регистрация, авторизация и создание рецепта.

Сайт: https://foodgram-frontend-1.foodgram.education-services.ru

## Структура

conftest.py        # фикстуры: driver (Chrome), registered_user, authorized_driver
urls.py            # адреса страниц
data.py            # тестовые данные (ингредиент, время, описание, название рецепта)
users.py           # учётные данные пользователя
helpers.py         # генерация данных пользователя
locators/          # локаторы страниц (header, signin, signup, recipes)
pages/             # Page Object: base, signin, signup, recipes, recipe_create
tests/             # тесты: test_signup, test_signin, test_recipe_create
assets/pic.jpeg    # фото для загрузки при создании рецепта
