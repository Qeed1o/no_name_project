from Card import Card, CARD_TYPE

class User:
    def __init__(self, name: str, cards: list[Card]):
        self.name = name
        self.cards = cards
        self.money = 0

    def add_card(self, card: Card):
        self.cards.append(card)
    
    def do_move(self, roll: int, turn: bool):
        for card in self.cards:
            if card.roll == roll and card.type == CARD_TYPE.get("Синяя"):
                self.money += card.calculate_bonus(self.cards)
                print("%s карточка отработала!!!" % card.name)
            if card.roll == roll and turn is True and card.type == CARD_TYPE.get("Зеленая"):
                self.money += card.calculate_bonus(self.cards)
                print("%s карточка отработала!!!" % card.name)
            if card.roll == roll and turn is False and card.type == CARD_TYPE.get("Красная"):
                pass