from Card import Card
import random

# BLUE


class WheatField(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class Farm(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class Cornfield(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        if len(user.attractions) <= 2:
            return 1
        else:
            return 0


class FlowerGarden(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class Vineyard(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 3


class Reserve(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class Mine(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 5


class FishingBoat(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        if "O2" in user.attractions:
            return 3
        else:
            return 0


class Trawler(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        names = [attraction.name for attraction in user.attractions]
        if "Порт" in names:
            return random.randint(2, 12)
        else:
            return 0


class AppleOrchard(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 3
