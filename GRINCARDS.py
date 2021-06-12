from Card import Card


# GREEN

class DepartmentStore(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 2


class Bakery(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class Supermarket(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 3


class DemolitionCompany(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 8


class CreditBureaus(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return -2


class FlowerShop(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        counter = 0
        for card in user:
            if card.key == "B4":
                counter += 1
        return counter


class CheeseDiary(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        counter = 0
        for card in user:
            if card.key == "B2":
                counter += 1
        return counter * 3


class FurnitureFactory(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        counter = 0
        for card in user:
            if card.key == "B6" or "B7":
                counter += 1
        return counter * 3


class WineFactory(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        counter = 0
        for card in user:
            if card.key == "B5":
                counter += 1
        return counter * 6


class TransportCompany(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class BeverageFactory(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        counter = 0
        for card in user:
            if card.type == 2:
                counter += 1
        return counter


class VegetableMarket(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        counter = 0
        for card in user:
            if card.key == "B1" or "B3" or "B4" or "B5":
                counter += 1
        return counter * 2


class GroceryWarehouse(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        counter = 0
        for card in user:
            if card.type == 2:
                counter += 1
        return counter * 2
