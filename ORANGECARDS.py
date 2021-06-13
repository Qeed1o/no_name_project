import random
from Attraction import Attractions


class Townhall(Attractions):
    def __init__(self, name: str, cost: int, type: int, flip: bool):
        super().__init__(name, cost, type, flip)

    def calculate_bonus_after_turn(self, user):
        if user.money == 0:
            user.money += 1
        pass


class Port(Attractions):
    def __init__(self, name: str, cost: int, type: int, flip: bool):
        super().__init__(name, cost, type, flip)

    def calculate_bonus_before_turn(self, user):
        pass


class Bank(Attractions):
    def __init__(self, name: str, cost: int, type: int, flip: bool):
        super().__init__(name, cost, type, flip)

    def calculate_bonus_before_turn(self, user):
        if random.randint(1, 100) == 27:
            user.money += 3
            return user.money


class Railwaystation(Attractions):
    def __init__(self, name: str, cost: int, type: int, flip: bool):
        super().__init__(name, cost, type, flip)

    def calculate_bonus_before_turn(self, user):
        return 1


class Mall(Attractions):
    def __init__(self, name: str, cost: int, type: int, flip: bool):
        super().__init__(name, cost, type, flip)

    def calculate_bonus(self, user):
        return 1


class TVTower(Attractions):
    def __init__(self, name: str, cost: int, type: int, flip: bool):
        super().__init__(name, cost, type, flip)

    def calculate_bonus(self, user):
        return 1


class AmusementPark(Attractions):
    def __init__(self, name: str, cost: int, type: int, flip: bool):
        super().__init__(name, cost, type, flip)

    def calculate_bonus(self, user):
        return 1


class Waterpark(Attractions):
    def __init__(self, name: str, cost: int, type: int, flip: bool):
        super().__init__(name, cost, type, flip)

    def calculate_bonus(self, user):
        return 1


class Airport(Attractions):
    def __init__(self, name: str, cost: int, type: int, flip: bool):
        super().__init__(name, cost, type, flip)

    def calculate_bonus(self, user):
        return 1
