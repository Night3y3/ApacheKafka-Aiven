import random
from faker.providers import BaseProvider

class PizzaProvider(BaseProvider):
    def pizza(self):
        pizzas = ['Margherita', 'Marinara', 'Carbonara', 'Frutti di Mare', 'Quattro Stagioni', 'Crudo', 'Napoletana', 'Pugliese', 'Montanara', 'Emiliana', 'Romana', 'Fattoria', 'Schiacciata', 'Prosciutto', 'Americana', 'Tonno', 'Capricciosa', 'Viennese', 'Boscaiola', 'Diavola', 'Pugliese', 'Ortolana', 'Pesto', 'Tartufata', 'Quattro Formaggi', 'Quattro Stagioni', 'Rustica', 'Siciliana', 'Vegetariana', 'Sarda', 'Tedesca', 'Valtellina', 'Piemontese', 'Parmigiana', 'Gorgonzola', 'Bufalina', 'Bianca', 'Bismarck', 'Bari', 'Bolognese', 'Calzone', 'Calabrese', 'Carciofi', 'Cipolla', 'Diavola', 'Focaccia', 'Friggitelli', 'Funghi', 'Gorgonzola', 'Grana', 'Mare e Monti', 'Mediterranea', 'Melanzane', 'Napoletana', 'Parmigiana', 'Patate', 'Peperoni', 'Pugliese', 'Quattro Formaggi', 'Radicchio', 'Rucola', 'Salsiccia', 'Siciliana', 'Spinaci', 'Tartufo', 'Tartufata', 'Tonno', 'Valtellina', 'Verdure', 'Zola']

        return pizzas[random.randint(0,len(pizzas) - 1)]