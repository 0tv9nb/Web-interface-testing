from random import random

from data.data import DataToFill, DataToColor
from faker import Faker
import random

faker_ru = Faker('ru_RU')  # to generate Russian text


# Faker.seed()


def generated_data():
    yield DataToFill(
        full_name=faker_ru.name(),
        mail=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(14, 100),
        salary=random.randint(1000, 100000),
        department=faker_ru.job(),
    )


def generated_color(k=1):
    colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    yield DataToColor(
        color=random.sample(colors, k)
    )
