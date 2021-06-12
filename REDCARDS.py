from Card import Card


# RED

class SushiBar(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class Cafe(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class Restaurant(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class Pizzeria(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class BurgerJoint(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class Eatery(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class LuxuryBar(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1
