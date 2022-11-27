'''
No Blackjack, o jogador pode apostar um valor qualquer x. Ao ganhar, de maneira geral, o jogador receberá 2x o valor de sua aposta.
Quando o jogador ganha com um Blackjack, ele receberá 2.5x o valor de sua aposta.
'''

import pyglet
from pathlib import Path
from ..game import game
from ..player import player
from src.botoes.botao_main import Widget

class Input(Widget):
    numeros = ["0","1","2","3","4","5","6","7","8","9"]
    
    def __init__(self, x, y, width, height, texto=""):
        super().__init__(x, y, width, height,texto)
        self.selecionado = False
        self.texto = texto
        self.moldura = pyglet.shapes.BorderedRectangle(x, y, width, height, color=(128,0,0), border_color=(255, 255, 255))
        self.linha = pyglet.shapes.Line(x, y + 5, x + width, y + 5)
        self.label = pyglet.text.Label(self.texto,
                font_name='Arial',
                font_size=32,
                anchor_x='center', anchor_y='center',
                x = self.x + self.width // 2,
                y = self.y + self.height // 2)
    def draw(self):
        if self.selecionado:
            self.moldura.draw()
        self.linha.draw()
        self.label.draw()
    def clica(self, x, y):
        self.selecionado = False
        super().clica(x, y)
    def on_click(self):
        self.selecionado = True
        self.label.text = "0"
        
    def digita(self, symbol):
        if not self.selecionado:
            return 
        if symbol == "BACKSPACE":
            self.label.text = self.label.text[0:-1]
        if symbol in numeros:
            self.label.text += symbol
        else:
            raise ValueError("Digite apenas números.")

    def __repr__(self):
        return f"Input '{self.texto}'" 

class Aposta(Input):   
    def __init__(self):
            self.valor = 0 #valor começa em 0
            super().__init__(x, y, width, height, texto=f'Valor da aposta: {self.valor}')
            
            
    nova_aposta(self): 
        super().digita()
        self.valor = super().__repr__()
        self.texto = f'Valor da aposta: {self.valor}'
        
   
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
      
