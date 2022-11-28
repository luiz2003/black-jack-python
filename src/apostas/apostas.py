'''
No Blackjack, o jogador pode apostar um valor qualquer x. Ao ganhar, de maneira geral, o jogador receberá 2x o valor de sua aposta.
Quando o jogador ganha com um Blackjack, ele receberá 3x o valor de sua aposta.
'''

import pyglet
from pathlib import Path
from ..game import game
from ..player import player
from src.botoes.botao_main import Widget


class Aposta(Widget):
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def __init__(self, x, y, width, height, texto=""):
        super().__init__(x, y, width, height, texto)
        self.selecionado = False
        self.texto = texto
        self.moldura = pyglet.shapes.BorderedRectangle(x, y, width, height, color=(128, 0, 0),
                                                       border_color=(255, 255, 255))
        self.linha = pyglet.shapes.Line(x, y + 5, x + width, y + 5)
        self.label = pyglet.text.Label(self.texto,
                                       font_name='Arial',
                                       font_size=32,
                                       anchor_x='center', anchor_y='center',
                                       x=self.x + self.width // 2,
                                       y=self.y + self.height // 2)

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
        if symbol in Aposta.numeros:
            self.label.text += symbol
        else:
            raise ValueError("Erro, digite apenas números!")

    def __repr__(self):
        return f"Input '{self.texto}'"
