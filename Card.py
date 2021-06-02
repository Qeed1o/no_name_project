class Card:
    def __init__(self, name: str, cost: int, roll: int, type: int):
        self.name = name
        self.cost = cost
        self.roll = roll
        self.type = type

    def calculate_bonus(self, cards):
        return 0

CARD_TYPE = {
    "Синяя": 0,
    "Зеленая": 1,
    "Красная": 2
}

class Bakery(Card):
    def __init__(self, name: str, cost: int, roll: int, type: int):
        super().__init__(name, cost, roll, type)
    
    def calculate_bonus(self, cards):
        return 1

class Field(Card):
    def __init__(self, name: str, cost: int, roll: int, type: int):
        super().__init__(name, cost, roll, type)
    
    def calculate_bonus(self, cards):
        return 1

class CheeseDiary(Card):
    def __init__(self, name: str, cost: int, roll: int, type: int):
        super().__init__(name, cost, roll, type)
    
    def calculate_bonus(self, cards):
        counter = 0
        for card in cards:
            if card.name is "Ферма":
                counter += 1
        return counter * 3

class Farm(Card):
    def __init__(self, name: str, cost: int, roll: int, type: int):
        super().__init__(name, cost, roll, type)
    def calculate_bonus(self, cards):
        return 1

class Shop(Card):
    def __init__(self, name: str, cost: int, roll: int, type: int):
        super().__init__(name, cost, roll, type)
    def calculate_bonus(self, cards):
        return 3



CARDS = {
    "Пекарня": Bakery(name="Пекарня", cost=1, roll=2, type=CARD_TYPE.get('Зеленая')),
    "Пшеничное поле": Field(name="Пшеничное поле", cost=1, roll=1, type=CARD_TYPE.get('Синяя')),
    "Ферма": Farm(name="Ферма", cost=1, roll=2, type=CARD_TYPE.get('Синяя')),
    "Сыроварня": CheeseDiary(name="Сыроварня", cost=5, roll=6, type=CARD_TYPE.get('Зеленая')),
    "Магазин": Shop(name="Магазин", cost=2, roll=4, type=CARD_TYPE.get('Зеленая'))
}