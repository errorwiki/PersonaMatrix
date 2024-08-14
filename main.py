import os
import random
import secrets
import string
from datetime import datetime, timedelta
from fake_useragent import UserAgent


def main():
    script_dir = os.path.dirname(__file__)

    with open(script_dir + '/data/german/first-names.txt', 'r') as file:
        first_names = file.read().splitlines()
    with open(script_dir + '/data/german/last-names.txt', 'r') as file:
        last_names = file.read().splitlines()
    with open(script_dir + '/data/german/streets.txt', 'r') as file:
        streets = file.read().splitlines()
    with open(script_dir + '/data/german/cities.txt', 'r') as file:
        cities = file.read().splitlines()
    with open(script_dir + '/data/german/zip-codes.txt', 'r') as file:
        zip_codes = file.read().splitlines()
    with open(script_dir + '/data/german/mobile-numbers.txt', 'r') as file:
        mobile_numbers = file.read().splitlines()

    user = User(first_names, last_names, streets, cities, zip_codes, mobile_numbers)
    print(user)


class User:
    def __init__(self, first_names, last_names, streets, cities, zip_codes, mobile_numbers):
        self.first_name = random.choice(first_names)
        self.last_name = random.choice(last_names)
        self.street = random.choice(streets)
        self.house_number = random.randint(1, 100)
        self.city = random.choice(cities)
        self.zip_code = random.choice(zip_codes)
        self.email = f'{self.first_name.lower()}.{self.last_name.lower()}@gmail.com'
        self.phone = random.choice(mobile_numbers)
        self.birthday = ((datetime.now() - timedelta(days=365*90))
                         + timedelta(days=random.randint(0, (365*90))))
        self.age = (datetime.now().year - self.birthday.year
                    - ((datetime.now().month, datetime.now().day) < (self.birthday.month, self.birthday.day)))
        self.username = f'{self.first_name.lower()}{self.last_name.lower()}{random.randint(1, 1000)}'
        self.password = "".join([secrets.choice(string.digits + string.ascii_letters + '!@#$%^&*()')
                                 for _ in range(24)])
        self.user_agent = UserAgent().random

    def __str__(self):
        return (f'{self.first_name} {self.last_name}\n'
                f'{self.street} {self.house_number}\n'
                f'{self.zip_code} {self.city}\n\n'
                f'Email: {self.email}\n'
                f'Phone: {self.phone}\n'
                f'Birthday: {self.birthday.strftime("%B %d, %Y")}\n'
                f'Age: {self.age}\n'
                f'Username: {self.username}\n'
                f'Password: {self.password}\n'
                f'User Agent: {self.user_agent}'
                )


if __name__ == '__main__':
    main()
