from ..cartas.baralho import Baralho

class Dealer:
    def __init__(self) -> None:
        self.deck = []
        self.hand = []
    
    def pull_card(self, player):
        player.hand.add_card(self.deck.pop())
    
    def start_game(self, player):
        self.deck = Baralho()
        self.deck.shuffle()

        player.hand.add_card(self.deck.pop())
        player.hand.add_card(self.deck.pop())
        
        self.hand.add_card(self.deck.pop())
        self.hand.add_card(self.deck.pop())
        print("Carta do dealer:", self.hand[0])

    def total_value(self):
        value = 0
        for card in self.hand:
            value += card.get_value(card, self.hand)
        return value
        
    