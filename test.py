from src.cartas import baralho
from src.dealer import dealer
from src.player import player
from src.cartas import cartas

Carta = cartas.Carta

print("Começando o jogo ...")

deck = baralho.Baralho()

dealer = dealer.Dealer()

player = player.Player()

dealer.start_game(player)

playerComBlackJack = player.Player()
playersemBlackJack = player.Player()

playerComBlackJack.hand.extend([Carta("Paus", 10), Carta("Paus", "K")])
playersemBlackJack.hand.extend([Carta("Paus", 10), Carta("Paus", 5)])

print(playerComBlackJack.hasBlackJack())
print(playersemBlackJack.hasBlackJack())

while True:
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
            break
    else:
        if dealer.total_value > 21:
            print("Você ganhou. O dealer estourou!")
            break
        if player.total_value > dealer.total_value:
            print("Parabéns! Você ganhou")
            break
        else: 
            print("O dealer conseguiu um valor maior! Você perde")
            break


