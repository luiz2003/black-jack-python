
class Player:
    def __init__(self) -> None:
        self.hand = []
        self._total_value = 0

    def add_card(self, card):
        self.hand.append(card)
    
    @property
    def total_value(self):
        value = 0
        for card in self.hand:
            value += card.get_value(self.hand)
        return value

    def show_hand(self):
        print("Sua mão :", *self.hand)
 