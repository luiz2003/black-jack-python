import random

class Carta:
    def __init__(self,  naipe, value):
        self.value = value
        self.naipe = naipe
    
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


#Carta = cartas.Carta

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

class Player:
    def __init__(self) -> None:
        self.hand = []
        self._total_value = 0

    def add_card(self, card):
        self.hand.append(card)
    
    @property
    def total_value(self):
        value = 0
        for card in self.hand:
            value += card.get_value(self.hand)
        return value

    def show_hand(self):
        print("Sua mão :", *self.hand)
 

class Dealer(Player):
    def pull_card(self, player):
        player.add_card(self.deck.pop())
    
    
    def start_game(self, player):
        self.deck = Baralho()
        self.deck.shuffle()

        player.add_card(self.deck.pop())
        player.add_card(self.deck.pop())
        
        self.add_card(self.deck.pop())
        self.add_card(self.deck.pop())
        print("Carta do dealer:", self.hand[0])

class Aposta:
    TETO_INICIAL = 1500
    
    def __init__(self, valor, teto=TETO_INICIAL):
        self._teto = teto
        
        if valor > 0 and valor <= teto:
            self.valor = valor
        else:
            print("Aposta inválida.")
    
    def get_teto(self):
        return self._teto
    
    def aumentar_teto(self, contador_partidas):
        if contador_partidas > 0:
            self._teto = 2 * self._teto 
    
    def resetar_teto(self, contador_partidas):
        if contador_partidas == 0:
            self._teto = 1500
            
    def nova_aposta(self, novo_valor):
        if novo_valor > 0 and novo_valor <= self._teto:
            self.valor = novo_valor
        else:
            print("Aposta inválida.")

print("Começando o jogo ...")
print("Insira um valor entre 0 e", Aposta.TETO_INICIAL)
a = int(input())

aposta = Aposta(a)
deck = Baralho()
dealer = Dealer()
player = Player()

dealer.start_game(player)

while True:
    contador_partidas = 0
    player.show_hand()
    res = input("Quer outra carta? [y/n]")
    
    if res == "y" :
        dealer.pull_card(player)
        player.show_hand()
        if player.total_value > 21 and dealer.total_value > 21:
            print("É um empate!")
            break
        elif player.total_value > 21 :
            print("Seu valor passou de 21, você perdeu!")
            contador_partidas = 0
            aposta.resetar_teto(contador_partidas)
            break
    else:
        if dealer.total_value > 21:
            print("Você ganhou. O dealer estourou!")
            aposta.aumentar_teto(contador_partidas)
            contador_partidas += 1
            break
        if player.total_value > dealer.total_value:
            print("Parabéns! Você ganhou")
            contador_partidas += 1
            aposta.aumentar_teto(contador_partidas)
            break
        else: 
            print("O dealer conseguiu um valor maior! Você perde")
            contador_partidas = 0
            aposta.resetar_teto(contador_partidas)
            break

print(contador_partidas)
