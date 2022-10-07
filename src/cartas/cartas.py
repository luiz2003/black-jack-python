from pathlib import Path
import pyglet
class Carta:
    def __init__(self,  naipe, value):
        self.value = value
        self.naipe = naipe
        self.image = pyglet.image.load(Path("../sprites/" + value + naipe))
    
    
    def get_value(self, hand):
        
        if self.value in ["Valete", "Rainha", "Rei"]:
            return 10
        
        if self.value != "A":
            return self.value 
        
        for card in hand:
            if card.value in ["Valete", "Rainha", "Rei"]:
                return 1

        return 11
        
        

    def __repr__(self) -> str:
        return str(self.value) + " " + self.naipe
