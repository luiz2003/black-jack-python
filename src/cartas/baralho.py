import random
from . import cartas
import pyglet

Carta = cartas.Carta

class Baralho:
    def __init__(self)->None:
        self.cards = []
        for naipe in ["Paus", "Copas", "Espadas", "Ouro"]:
            for i in range(1,12):
                if i == 1:
                    self.cards.append(Carta( naipe, "A"))
                    continue
                if i <=10:
                    self.cards.append(Carta( naipe, i))
                    continue
                for j in ["Valete", "Rainha", "Rei"]:
                    self.cards.append(Carta( naipe, j))

    def pop(self) -> cartas.Carta :
        return self.cards.pop()

    def shuffle(self)->None:
        for i in range (len(self.cards)-1,0,-1):
            r = random.randint(0 , i)
            self.cards[i]  , self.cards[r] = self.cards[r] , self.cards[i]
                
