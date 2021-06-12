import random


class Card:
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        self.name = name
        self.cost = cost
        self.roll = roll
        self.type = type
        self.ID = ID

    def calculate_bonus(self, cards):
        return 0
CARD_TYPE = {
    "Синяя": 0,
    "Зеленая": 1,
    "Красная": 2,
    "Фиолетовая": 3
}

# BLUE
class WheatField(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class Farm(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class Cornfield(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class FlowerGarden(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class Vineyard(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 3


class Reserve(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class Mine(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 5


class FishingBoat(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 3


class Trawler(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return random.randint(2, 12)


class AppleOrchard(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 3


#GREEN

class DepartmentStore(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 2


class Bakery(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class Supermarket(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 3


class DemolitionCompany(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 8


class CreditBureaus(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return -2


class FlowerShop(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        counter = 0
        for card in cards:
            if card.ID == "B4":
                counter += 1
        return counter


class CheeseDiary(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        counter = 0
        for card in cards:
            if card.ID == "B2":
                counter += 1
        return counter * 3


class FurnitureFactory(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        counter = 0
        for card in cards:
            if card.ID == "B6" or "B7":
                counter += 1
        return counter * 3


class WineFactory(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        counter = 0
        for card in cards:
            if card.ID == "B5":
                counter += 1
        return counter * 6


class TransportCompany(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class BeverageFactory(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        counter = 0
        for card in cards:
            if card.type == 2:
                counter += 1
        return counter


class VegetableMarket(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        counter = 0
        for card in cards:
            if card.ID == "B1" or "B3" or "B4" or "B5":
                counter += 1
        return counter * 2


class GroceryWarehouse(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        counter = 0
        for card in cards:
            if card.type == 2:
                counter += 1
        return counter * 2

#RED

class SushiBar(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class Cafe(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class Restaurant(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class Pizzeria(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class BurgerJoint(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class Eatery(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class LuxuryBar(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1

#VIOLET

class Stadium(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class Telecentre(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class BusinessCenter(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class Publishing(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class BuildingRepairCompany(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class TaxService(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class VentureFund(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class ConcertCenter(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


class Park(Card):
    def __init__(self, name: str, cost: int, roll: list, type: int, ID: str):
        super().__init__(name, cost, roll, type, ID)

    def calculate_bonus(self, cards):
        return 1


CARDS = {
    "Пшеничное поле": WheatField(name="Пшеничное поле", cost=1, roll=[1], type=CARD_TYPE.get('Синяя'), ID='B1'),
    "Ферма": Farm(name="Ферма", cost=1, roll=[2], type=CARD_TYPE.get('Синяя'), ID='B2'),
    "Кукурузное поле": Cornfield(name='Кукурузное поле', cost=2, roll=[3, 4], type=CARD_TYPE.get('Синяя'), ID='B3'),
    "Цветник": FlowerGarden(name='Цветник', cost=2, roll=[4], type=CARD_TYPE.get('Синяя'), ID='B4'),
    "Виноградник": Vineyard(name='Виноградник', cost=3, roll=[7], type=CARD_TYPE.get('Синяя'), ID='B5'),
    "Заповедник": Reserve(name='Заповедник', cost=3, roll=[5], type=CARD_TYPE.get('Синяя'), ID='B6'),
    "Рудник": Mine(name='Рудник', cost=6, roll=[9], type=CARD_TYPE.get('Синяя'), ID='B7'),
    "Рыбацкий баркас": FishingBoat(name='Рыбацкий баркас', cost=2, roll=[8], type=CARD_TYPE.get('Синяя'), ID='B8'),
    "Траулер": Trawler(name='Траулер', cost=5, roll=[12, 13, 14], type=CARD_TYPE.get('Синяя'), ID='B9'),
    "Яблоневый сад": AppleOrchard(name='Яблоневый сад', cost=3, roll=[10], type=CARD_TYPE.get('Синяя'), ID='B10'),

    "Универмаг": DepartmentStore(name="Универмаг", cost=1, roll=[2], type=CARD_TYPE.get('Зеленая'), ID='G1'),
    "Пекарня": Bakery(name="Пекарня", cost=1, roll=[2], type=CARD_TYPE.get('Зеленая'), ID='G2'),
    "Супермаркет": Supermarket(name="Супермаркет", cost=2, roll=[4], type=CARD_TYPE.get('Зеленая'), ID='G3'),
    "Компания по сносу зданий": DemolitionCompany(name="Компания по сносу зданий", cost=2, roll=[4],
                                                  type=CARD_TYPE.get('Зеленая'), ID='G4'),
    "Кредитное бюро": CreditBureaus(name="Кредитное бюро", cost=0, roll=[5, 6], type=CARD_TYPE.get('Зеленая'), ID='G5'),
    "Цветочный магазин": FlowerShop(name="Цветочный магазин", cost=1, roll=[6], type=CARD_TYPE.get('Зеленая'), ID='G6'),
    "Сыроварня": CheeseDiary(name="Сыроварня", cost=5, roll=[7], type=CARD_TYPE.get('Зеленая'), ID='G7'),
    "Мебельная фабрика": FurnitureFactory(name="Мебельная фабрика", cost=3, roll=[8], type=CARD_TYPE.get('Зеленая'), ID='G8'),
    "Винный завод": WineFactory(name="Винный завод", cost=2, roll=[9], type=CARD_TYPE.get('Зеленая'), ID='G9'),
    "Транспортная компания": TransportCompany(name="Транспортная компания", cost=2, roll=[9, 10],
                                              type=CARD_TYPE.get('Зеленая'), ID='G10'),
    "Фабрика напитков": BeverageFactory(name="Фабрика напитков", cost=5, roll=[11], type=CARD_TYPE.get('Зеленая'), ID='G11'),
    "Овощной рынок": VegetableMarket(name="Овощной рынок", cost=2, roll=[11, 12], type=CARD_TYPE.get('Зеленая'), ID='G12'),
    "Продуктовый склад": GroceryWarehouse(name="Продуктовый склад", cost=2, roll=[12, 13],
                                          type=CARD_TYPE.get('Зеленая'), ID='G13'),

    "Суши бар": SushiBar(name="Суши бар", cost=4, roll=[1], type=CARD_TYPE.get('Красная'), ID='R1'),
    "Кафе": Cafe(name="Кафе", cost=2, roll=[3], type=CARD_TYPE.get('Красная'), ID='R2'),
    "Ресторан": Restaurant(name="Ресторан", cost=3, roll=[5], type=CARD_TYPE.get('Красная'), ID='R3'),
    "Пиццерия": Pizzeria(name="Пиццерия", cost=1, roll=[7], type=CARD_TYPE.get('Красная'), ID='R4'),
    "Бургерная": BurgerJoint(name="Бургерная", cost=1, roll=[8], type=CARD_TYPE.get('Красная'), ID='R5'),
    "Закусочная": Eatery(name="Закусочная", cost=3, roll=[9, 10], type=CARD_TYPE.get('Красная'), ID='R6'),
    "Элитный бар": LuxuryBar(name="Элитный бар", cost=4, roll=[12, 13, 14], type=CARD_TYPE.get('Красная'), ID='R7'),

    "Стадион": Stadium(name="Стадион", cost=6, roll=[6], type=CARD_TYPE.get('Фиолетовая'), ID='V1'),
    "Телецентр": Telecentre(name="Телецентр", cost=7, roll=[6], type=CARD_TYPE.get('Фиолетовая'), ID='V2'),
    "Бизнес цетр": BusinessCenter(name="Бизнес цетр", cost=8, roll=[6], type=CARD_TYPE.get('Фиолетовая'), ID='V3'),
    "Издательство": Publishing(name="Издательство", cost=5, roll=[7], type=CARD_TYPE.get('Фиолетовая'), ID='V4'),
    "Компания по ремонту зданий": BuildingRepairCompany(name="Компания по ремонту зданий", cost=4, roll=[8],
                                                        type=CARD_TYPE.get('Фиолетовая'), ID='V5'),
    "Налоговая": TaxService(name="Налоговая", cost=4, roll=[8, 9], type=CARD_TYPE.get('Фиолетовая'), ID='V6'),
    "Венчурный фонд": VentureFund(name="Венчурный фонд", cost=1, roll=[10], type=CARD_TYPE.get('Фиолетовая'), ID='V7'),
    "Концерт центр": ConcertCenter(name="Концерт центр", cost=7, roll=[10], type=CARD_TYPE.get('Фиолетовая'), ID='V8'),
    "Парк": Park(name="Парк", cost=3, roll=[11, 12, 13], type=CARD_TYPE.get('Фиолетовая'), ID='V9')
}


second_user = User(name="test2", cards=[CARDS.get("Траулер")])
print(second_user)