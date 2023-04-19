from random import random

from data.data import DataToFill, DataToColor, DataToDate
from faker import Faker
import random
import datetime

faker_ru = Faker('ru_RU')  # to generate Russian text
faker_en = Faker('En')


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
    times = {0: '00:00', 1: '00:15', 2: '00:30', 3: '00:45', 4: '01:00', 5: '01:15', 6: '01:30', 7: '01:45', 8: '02:00',
             9: '02:15', 10: '02:30', 11: '02:45', 12: '03:00', 13: '03:15', 14: '03:30', 15: '03:45', 16: '04:00',
             17: '04:15', 18: '04:30', 19: '04:45', 20: '05:00', 21: '05:15', 22: '05:30', 23: '05:45', 24: '06:00',
             25: '06:15', 26: '06:30', 27: '06:45', 28: '07:00', 29: '07:15', 30: '07:30', 31: '07:45', 32: '08:00',
             33: '08:15', 34: '08:30', 35: '08:45', 36: '09:00', 37: '09:15', 38: '09:30', 39: '09:45', 40: '10:00',
             41: '10:15', 42: '10:30', 43: '10:45', 44: '11:00', 45: '11:15', 46: '11:30', 47: '11:45', 48: '12:00',
             49: '12:15', 50: '12:30', 51: '12:45', 52: '13:00', 53: '13:15', 54: '13:30', 55: '13:45', 56: '14:00',
             57: '14:15', 58: '14:30', 59: '14:45', 60: '15:00', 61: '15:15', 62: '15:30', 63: '15:45', 64: '16:00',
             65: '16:15', 66: '16:30', 67: '16:45', 68: '17:00', 69: '17:15', 70: '17:30', 71: '17:45', 72: '18:00',
             73: '18:15', 74: '18:30', 75: '18:45', 76: '19:00', 77: '19:15', 78: '19:30', 79: '19:45', 80: '20:00',
             81: '20:15', 82: '20:30', 83: '20:45', 84: '21:00', 85: '21:15', 86: '21:30', 87: '21:45', 88: '22:00',
             89: '22:15', 90: '22:30', 91: '22:45', 92: '23:00', 93: '23:15', 94: '23:30', 95: '23:45'}
    rand = random.randint(1, 96)
    random_date = faker_en.date_time()
    yield DataToDate(
        year=random_date.year,
        month=random_date.strftime('%B'),
        day=random_date.strftime('%d'),
        tim=[times[rand], rand]
    )
