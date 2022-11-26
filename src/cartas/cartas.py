from __future__ import annotations
from pathlib import Path
import pyglet
from typing import Union
from enum import Enum

class Naipes(Enum):
    PAUS = "Paus"
    COPAS = "Copas"
    ESPADAS = "Espadas"
    OURO = "Ouro"

class Court(Enum):
    VALETE = "Valete"
    RAINHA = "Rainha"
    REI = "Rei"
    ACE = "A"

class Carta:
    def __init__(self,  naipe: Naipes, value: Union[str,int]) -> None:
        
        if value not in ([member.value for member in Court] + [i for i in range(1, 11)]):
            raise ValueError("Invalid value for card")

        if naipe not in [suit for suit in Naipes]:
            raise ValueError("Invalid card suit")

        self._value = value
        self._naipe = naipe
        image = pyglet.image.load(Path('./sprites/'+ str(value) + str(naipe.value) + ".png").resolve())
        self.sprite = pyglet.sprite.Sprite(image)
    
    
    def convert_value(self, hand: list[Carta])-> int:
        
        if self._value in ["Valete", "Rainha", "Rei"]:
            return 10
        
        if self._value != "A":
            return int(self._value)
        
        for card in hand:
            if card._value in ["Valete", "Rainha", "Rei"]:
                return 1

        return 11
        
        

    def __repr__(self) -> str:
        return str(self._value) + " " + self._naipe.value

    def __eq__(self, o)-> bool:
      return self._value == o.value and self._naipe.value == o.naipe.value
