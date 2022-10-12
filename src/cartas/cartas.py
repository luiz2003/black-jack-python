from pathlib import Path
import pyglet
class Carta:
    def __init__(self,  naipe, value):
        self.value = value
        self.naipe = naipe
        image = pyglet.image.load(Path('./sprites/'+ str(value) + naipe + ".png").resolve())
        self.sprite = pyglet.sprite.Sprite(image)
    
    
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

    def __eq__(self, o):
      return self.value == o.value and self.naipe == o.naipe
