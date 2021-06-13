class Card:
    def __init__(self, name: str, cost: int, roll: list, type: int):
        self.name = name
        self.cost = cost
        self.roll = roll
        self.type = type
        self.closed_for_repairs = False

    def calculate_bonus(self, user):
        return 0

    def calculate_bonus_red(self, user, cur_money):
        return 0

    def calculate_bonus_red_with_attraction(self, user, cur_money, num_cur_attractions):
        return 0


    def to_dict(self):
        return {
            'name': self.name.encode().decode('utf-8'),
            'cost': self.cost,
            'roll': self.roll,
        }


CARD_TYPE = {
    "Синяя": 0,
    "Зеленая": 1,
    "Красная": 2,
    "Фиолетовая": 3,
    "Оранжевая": 4
}
