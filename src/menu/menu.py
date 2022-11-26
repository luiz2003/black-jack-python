import pyglet
from pathlib import Path
from src.botoes.botao_main import Botao
import webbrowser
from ..game import game
Game = game.Game

class MeuMenu(pyglet.window.Window):
    def __init__(self, width, height):
        super().__init__(width, height,
            caption="BlackJack")

        self.btn_ajuda = Botao(50, self.height//2 - 175, 200, 70, "Regras",self.regras)
        self.btn_sair = Botao(679, self.height//2 - 175, 200, 70, "Sair",self.sair)
        self.btn_comecar = Botao(self.width//2 - 150,self.height//2 - 225,300,70,"Vamos Jogar",self.comecar)
        self.fundo = pyglet.image.load(Path('sprites/fundomenu.jpg'))
        self.background = pyglet.sprite.Sprite(self.fundo)
        self.widgets = [self.btn_ajuda, self.btn_sair,self.btn_comecar]
        self.titulo_label = pyglet.text.Label('BlackJack',
                        color = (255,255,0,255),
                        font_name='Times New Roman',
                        font_size=72,
                        x=self.width//2, y=self.height//2 + 150,
                        anchor_x='center', anchor_y='center')

    def sair(self)->None:
        self.close()

    def regras(self)->None:
        webbrowser.open("https://www.pokerstars.com/pt-BR/casino/how-to-play/blackjack/rules/")

    def comecar(self):
        game = Game()
        pyglet.app.run()
 
    def on_draw(self)->None:
        self.clear()
        self.background.draw()
        for widget in self.widgets:
            widget.draw()
        self.titulo_label.draw()
    
    def on_mouse_press(self, x:int , y:int , button:int , modifiers:int) -> None:
        if not(isinstance(x, int) or isinstance(y,int)):
            raise ValueError("Invalid value for x or y")
        
        for widget in self.widgets:
            widget.clica(x, y)