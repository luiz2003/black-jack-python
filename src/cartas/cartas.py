from pathlib import Path
import pyglet
class Carta:
    def __init__(self,  naipe, value):
        
        if value not in (["Valete", "Rainha", "Rei", "A"] + [i for i in range(1, 11)]):
            raise ValueError("Invalid value for card")

        if naipe not in ["Paus", "Copas", "Espadas", "Ouro"]:
            raise ValueError("Invalid card suit")

        self._value = value
        self._naipe = naipe
        image = pyglet.image.load(Path('./sprites/'+ str(value) + naipe + ".png").resolve())
        self.sprite = pyglet.sprite.Sprite(image)
    
    
    def convert_value(self, hand):
        
        if self._value in ["Valete", "Rainha", "Rei"]:
            return 10
        
        if self._value != "A":
            return self._value 
        
        for card in hand:
            if card._value in ["Valete", "Rainha", "Rei"]:
                return 1

        return 11
        
        

    def __repr__(self) -> str:
        return str(self._value) + " " + self._naipe

    def __eq__(self, o):
      return self._value == o.value and self._naipe == o.naipe
