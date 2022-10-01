from ..cartas import baralho
from ..player import player

class Dealer(player.Player):
    def pull_card(self, player):
        player.add_card(self.deck.pop())
    
    
    def start_game(self, player):
        self.deck = baralho.Baralho()
        self.deck.shuffle()

        player.add_card(self.deck.pop())
        player.add_card(self.deck.pop())
        
        self.add_card(self.deck.pop())
        self.add_card(self.deck.pop())
        print("Carta do dealer:", self.hand[0])

        
    