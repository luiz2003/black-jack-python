'''
No Blackjack, o jogador pode apostar um valor qualquer x. Ao ganhar, de maneira geral, o jogador receberá 2x o valor de sua aposta.
Quando o jogador ganha com um Blackjack, ele receberá 2.5x o valor de sua aposta.
'''

import pyglet
from pathlib import Path
from ..game import game
from ..player import player

class Aposta:   
    def __init__(self)->None:
            self.valor = 1500
   
    def resultado(self, indicador_partidas, indicador_blackjack):
        if indicador_partidas == "player_estourou" or indicador_partidas == "dealer_valormaior": #jogador perde
            label = pyglet.text.Label(f'Você perdeu {self.valor} fichas...',
                                font_name='Times New Roman',
                                font_size=30,
                                x=self._width//2, y=150,
                                anchor_x='center', anchor_y='center')
        elif indicador_partidas == "dealer_estourou" or indicador_partidas == "player_valormaior": #jogador ganha
            label = pyglet.text.Label(f'Você ganhou {self.valor*2} fichas!',
                                font_name='Times New Roman',
                                font_size=30,
                                x=self._width//2, y=150,
                                anchor_x='center', anchor_y='center')
        elif indicador_blackjack == True: #jogador ganha com blackjack
            label = pyglet.text.Label(f'Você perdeu {self.valor*2.5} fichas!',
                                font_name='Times New Roman',
                                font_size=30,
                                x=self._width//2, y=150,
                                anchor_x='center', anchor_y='center')
      
