from data.data import DataToFill
from faker import Faker

faker_ru = Faker('ru_RU')  # to generate Russian text
# Faker.seed()


def generated_data():
    yield DataToFill(
        full_name=faker_ru.name(),
        mail=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )
