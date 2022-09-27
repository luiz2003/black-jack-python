from cartas import Carta

class Baralho:
    def __init__(self):
        self.cards = []
        for naipe in ["Paus", "Copas", "Espada", "Ouro"]:
            for i in range(1,11):
                if i == 1:
                    self.cards.append(Carta( naipe, "A"))
                    continue
                if i < 10:
                    self.cards.append(Carta( naipe, i))
                    continue
                for j in ["Valete", "Rainha", "Rei"]:
                    self.cards.append(Carta( naipe, j))
                


baralho = Baralho()

print(baralho.cards)