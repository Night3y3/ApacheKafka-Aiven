from faker import Faker
from pizzaproducer import PizzaProvider

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
for i in range(10):
    print(fake.pizza())