
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

    def hasBlackJack(self):
      if self.hand[0].value in [10, "Rei", "Valetes", "Rainha", "A"]:
            valueSet = {self.hand[0].value, self.hand[1].value }
            return valueSet.difference({"Rei", "Valetes", "Rainha"}) == {"A"}
      return False

