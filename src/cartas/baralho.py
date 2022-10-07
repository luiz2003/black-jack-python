import random
from . import cartas
import pyglet

Carta = cartas.Carta

class Baralho:
    def __init__(self):
        self.cards = []
        for naipe in ["Paus", "Copas", "Espada", "Ouro"]:
            for i in range(1,12):
                if i == 1:
                    self.cards.append(Carta( naipe, "A"))
                    continue
                if i <=10:
                    self.cards.append(Carta( naipe, i))
                    continue
                for j in ["Valete", "Rainha", "Rei"]:
                    self.cards.append(Carta( naipe, j))

    def pop(self):
        return self.cards.pop()

    def shuffle(self):
        for i in range (len(self.cards)-1,0,-1):
            r = random.randint(0 , i)
            self.cards[i]  , self.cards[r] = self.cards[r] , self.cards[i]
                

if __name__ == "__main__":
    baralho = Baralho()

    print(baralho.cards)

    baralho.shuffle()

    print(baralho.cards)