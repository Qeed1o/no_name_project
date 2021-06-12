from Card import Card


# VIOLET

class Stadium(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class Telecentre(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class BusinessCenter(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class Publishing(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class BuildingRepairCompany(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class TaxService(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class VentureFund(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class ConcertCenter(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1


class Park(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus(self, user):
        return 1
