from faker import Faker
import os
import random

fake = Faker('en_UK')
#Faker.seed(random.randint(0, 1000))


def create_people():
    names = fake.name()
    address = fake.address()
    address_2 = fake.address()
    people = str (names + "\n" + address + "\n\n" + address_2)
    return people


print (create_people())
    


