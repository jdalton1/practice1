from abc import ABC, abstractmethod
from copy import copy

class Person(ABC):
    def __init__(self, name):
        self._name = name
        self._cart = []

    @abstractmethod
    def purchase(self,item, quantity):
        return

    def get_name(self):
        return self._name

    def show_cart_total(self):
        total = 0
        for item,quantity in self._cart:
            total += item.get_price() * quantity
        return f"{total:.2f}"

class Retail_Customer(Person):
    def purchase(self,item,quantity):
        self._cart.append([item,quantity])
        print(self._cart)


class Dealer(Person):
    def __init__(self, name, discount):

        super().__init__(name)
        self._discount = discount

    def purchase(self, item, quantity):
        item.discount(self._discount)
        self._cart.append([item, quantity])

class Item():
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def discount(self,percentage_off):
        self._price *= (100 - percentage_off) / 100
        self._price = round(self._price,2)

    def get_price(self):
        return self._price


jaren = Dealer("Jaren",25)
roses = Item("roses", 1.99)
teddyBear = Item("Teddy Bear", 24.99)

jaren.purchase(copy(roses),12)
jaren.purchase(copy(teddyBear), 1)
print(jaren.show_cart_total())

josh = Retail_Customer("Josh")
josh.purchase(roses, 2)
print(josh.show_cart_total())