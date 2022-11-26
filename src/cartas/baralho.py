import random
from . import cartas
Carta = cartas.Carta
import copy


class Baralho:
    def __init__(self)->None:
        self._cards = []
        for naipe in [suit for suit in cartas.Naipes]:
            for i in range(1,12):
                if i == 1:
                    self._cards.append(Carta( naipe, "A"))
                    continue
                if i <=10:
                    self._cards.append(Carta( naipe, i))
                    continue
                for j in ["Valete", "Rainha", "Rei"]:
                    self._cards.append(Carta( naipe, j))

    def pop(self) -> cartas.Carta :
        return self._cards.pop()

    @property
    def cards(self):
        return copy.deepcopy(self._cards)

    def shuffle(self)->None:
        for i in range (len(self._cards)-1,0,-1):
            r = random.randint(0 , i)
            self._cards[i]  , self._cards[r] = self._cards[r] , self._cards[i]
                
