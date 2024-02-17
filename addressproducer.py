import random
from faker.providers import BaseProvider

class AddressProvider(BaseProvider):
    def address(self):
        addresses = []