from ..cartas import baralho
from ..player import player


playerClass =  player.Player

class Dealer(player.Player):
    def pull_card(self, player: player.Player)->None:
        if not isinstance(player, playerClass):
            raise TypeError("pull_card method must receive an instance of Player")

        player.add_card(self.deck.pop())
    
    
    def start_game(self, player: player.Player) -> None:
        
        if not isinstance(player, playerClass):
            raise TypeError("pull_card method must receive an instance of Player") 
        
        self.deck = baralho.Baralho()
        self.deck.shuffle()

        player.add_card(self.deck.pop())
        player.add_card(self.deck.pop())
        
        self.add_card(self.deck.pop())
        self.add_card(self.deck.pop())

        print("Carta do dealer:", self.hand[0])

        
        

        

        
    