import random
import string


def generate_random_string(length=10):
    letters = string.ascii_lowercase + string.digits
    return "".join(random.choice(letters) for i in range(length))


def generate_user_data():
    base = generate_random_string(length=8)
    return {
        "email": f"{base}@test.ru",
        "username": f"user_{base}",
        "first_name": generate_random_string(length=6),
        "last_name": generate_random_string(length=8),
        "password": generate_random_string(length=10),
    }
