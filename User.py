from Card import Card, CARD_TYPE
from Attraction import Attractions


class User:
    def __init__(self, name: str, cards: list[Card], attractions: list[Card], uid: int):
        self.attractions = attractions
        self.buy_card = False
        self.name = name
        self.cards = cards
        self.money = 3
        self.uid = uid

    def to_dict(self):
        return {
            'name': self.name,
            'money': self.money,
            'cards': [card.to_dict() for card in self.cards]
        }

    def add_card(self, card: Card):
        self.cards.append(card)

    def add_attractions(self, attraction: Card):
        self.attractions.append(attraction)

    def do_move(self, roll: int, turn: bool):
        for attraction in self.attractions:
            attraction.calculate_bonus_before_turn(self)
        self.buy_card = False
        for card in self.cards:
            if roll in card.roll and turn is True and card.type == CARD_TYPE.get("Зеленая") and card.closed_for_repairs is False:
                self.money += card.calculate_bonus(self)
                if "O5" in self.attractions:
                    self.money += 1
                print("%s карточка отработала!!!" % card.name, roll, turn)
            if roll in card.roll and card.type == CARD_TYPE.get("Синяя") and card.closed_for_repairs is False:
                self.money += card.calculate_bonus(self)
                print("%s карточка отработала!!!" % card.name)
            if roll in card.roll and turn is True and card.type == CARD_TYPE.get("Фиолетовая") and card.closed_for_repairs is False:
                pass

        for attraction in self.attractions:
            attraction.calculate_bonus_after_turn(self)

    def do_move_red(self, roll: int, turn: bool, cur):
        for card in self.cards:
            if roll in card.roll and turn is False and card.type == CARD_TYPE.get(
                    "Красная") and card.closed_for_repairs is False and (card.name == "Ресторан" or card.name == "Элитный бар"):
                cur_money = cur.money
                cur.money -= card.calculate_bonus_red_with_attraction(self.cards, cur_money, len(cur.attractions))
                self.money += card.calculate_bonus_red_with_attraction(self.cards, cur_money, len(cur.attractions))
                print("%s карточка отработала!!!" % card.name, roll, turn, "fuck")
            elif roll in card.roll and turn is False and card.type == CARD_TYPE.get(
                    "Красная") and card.closed_for_repairs is False:
                cur_money = cur.money
                cur.money -= card.calculate_bonus_red(self.cards, cur_money)
                self.money += card.calculate_bonus_red(self.cards, cur_money)
                print("%s карточка отработала!!!" % card.name, roll, turn, self.name)
