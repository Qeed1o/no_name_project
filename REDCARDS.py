from Card import Card


# RED

class SushiBar(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus_red(self, user, cur_money):
        if "Порт" in user.attractions and cur_money >= 3:
            return 3
        elif "Порт" in user.attractions and cur_money > 0:
            return cur_money
        else:
            return 0


class Cafe(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus_red(self, user, cur_money):
        if cur_money > 0:
            return 1
        else:
            return 0


class Restaurant(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus_red_with_attraction(self, user, cur_money, num_cur_attractions):
        if num_cur_attractions >= 2:
            if cur_money >= 5:
                return 5
            elif cur_money > 0:
                return cur_money
            else:
                return 0
        else:
            return 0


class Pizzeria(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus_red(self, user, cur_money):
        if cur_money > 0:
            return 1
        else:
            return 0


class BurgerJoint(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus_red(self, user, cur_money):
        if cur_money > 0:
            return 1
        else:
            return 0


class Eatery(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus_red(self, user, cur_money):
        if cur_money >= 2:
            return 2
        elif cur_money > 0:
            return int(cur_money)
        else:
            return 0


class LuxuryBar(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int):
        super().__init__(name, cost, roll, type)

    def calculate_bonus_red_with_attraction(self, user, cur_money, num_cur_attractions):
        if num_cur_attractions >= 3:
            return cur_money
        else:
            return 0
