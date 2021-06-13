class Attractions:
    def __init__(self, name: str, cost: int, type: int, flip: bool):
        self.name = name
        self.cost = cost
        self.type = type
        self.flip = flip

    def to_dict(self):
        return {
            'name': self.name,
            'cost': self.cost,
            'flip': self.flip
        }

    def calculate_bonus_before_turn(self, user):
        pass

    def calculate_bonus_after_turn(self, user):
        pass
