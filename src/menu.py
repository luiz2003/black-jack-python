import pyglet
from pathlib import Path
import os
from src.botoes.botoes_menu import BotaoAjuda, BotaoSair, BotaoComecar, QuantiaInicial
import webbrowser
from src.game.mainclass import MeuJogo


class MeuMenu(pyglet.window.Window):
    def __init__(self, width, height):
        super().__init__(width, height,
            caption="BlackJack")

        self.input_aposta = QuantiaInicial(self.width//2 - 150, self.height//2 - 50, 300, 70, "Quantia Inicial:")
        self.btn_ajuda = BotaoAjuda(50, self.height//2 - 175, 200, 70, "Regras",self.regras)
        self.btn_sair = BotaoSair(679, self.height//2 - 175, 200, 70, "Sair",self.vazar)
        self.btn_comecar = BotaoComecar(self.width//2 - 150,self.height//2 - 225,300,70,"Vamos Jogar",self.comecar)
        self.fundo = pyglet.image.load(Path('sprites/fundomenu.jpg'))
        self.background = pyglet.sprite.Sprite(self.fundo)
        self.widgets = [self.btn_ajuda, self.btn_sair,self.input_aposta,self.btn_comecar]
        self.titulo_label = pyglet.text.Label('BlackJack',
                        color = (255,255,0,255),
                        font_name='Times New Roman',
                        font_size=72,
                        x=self.width//2, y=self.height//2 + 150,
                        anchor_x='center', anchor_y='center')

    def vazar(self):
        os._exit(0)

    def regras(self):
        webbrowser.open("https://www.pokerstars.com/pt-BR/casino/how-to-play/blackjack/rules/")

    def comecar(self):
        if int(self.input_aposta.label.text) > 0:
            aposta_inicial = self.input_aposta.label.text
            mygame = MeuJogo(640,480)
            icon1 = pyglet.image.load(Path('sprites/blackjack_icon.png'))
            mygame.set_icon(icon1)
            pyglet.app.run()
        else:
            print("Quantia Inválida !")
        
    def on_draw(self):
        self.clear()
        self.background.draw()
        #self.logo.blit(0,0)
        for widget in self.widgets:
            widget.draw()
        self.titulo_label.draw()
        
    def on_text(self, text):
        for widget in self.widgets:
            widget.digita(text)
        
    def on_key_press(self, symbol, modifiers):
        for widget in self.widgets:
            if symbol == pyglet.window.key.BACKSPACE:
                widget.digita("BACKSPACE")

    def on_mouse_press(self, x, y, button, modifiers):
        for widget in self.widgets:
            widget.clica(x, y)


window1 = MeuMenu(929,626)
icon = pyglet.image.load(Path('sprites/blackjack_icon.png'))
window1.set_icon(icon)


pyglet.app.run()