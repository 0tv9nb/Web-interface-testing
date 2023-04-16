from random import random

from data.data import DataToFill, DataToColor, DataToDate
from faker import Faker
import random

faker_ru = Faker('ru_RU')  # to generate Russian text
faker_en=Faker('En')

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


def generated_color(colors, k=1):
    yield DataToColor(
        color=random.sample(colors, k)
    )
def generated_date():
    yield DataToDate(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
    )