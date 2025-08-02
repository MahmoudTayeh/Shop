from faker import Faker
from account.models import CustomUser
from .models import Product
import random

faker = Faker()

def populate_users_and_products(count=5):
    for _ in range(count):
        CustomUser.objects.create(
            username=faker.name().capitalize(),
            phone_number=faker.phone_number(),
            email=faker.email(),
            address=faker.address(),
        )
        Product.objects.create(
            name=faker.name().capitalize(),
            description=faker.sentence(),
            price=round(random.uniform(5,100),2),
            img=None,
        )
