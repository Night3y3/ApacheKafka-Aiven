from faker import Faker
from pizzaproducer import PizzaProvider
from nameproducer import NameProvider

fake = Faker()

# message = {
#     'name' : fake.name(),
#     'address' : fake.address(),
#     'email' : fake.email(),
#     'text' : fake.text(),
#     'phone' : fake.phone_number(),
#     'job' : fake.job(),
#     'company' : fake.company(),
#     'date' : fake.date(),
# }

# print(message)

fake.add_provider(PizzaProvider)

def get_fake_name():
    return fake.name()

def get_fake_address():
    return fake.address()

def get_fake_email():
    return fake.email()

def get_fake_phone():
    return fake.phone_number()

def get_fake_pizza():
    return fake.pizza()
