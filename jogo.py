import pyglet
from pathlib import Path
from src.game.game import Game
from src.botoes.botoes_main import BotaoComprar, BotaoParar

class MeuJogo(pyglet.window.Window):
    def __init__(self, width, height):
        super().__init__(width, height,
            caption="BlackJack")
    
        self.batch = pyglet.graphics.Batch()
        self.cards = pyglet.graphics.OrderedGroup(1)
        self.background_group = pyglet.graphics.OrderedGroup(0)



        self.icon = pyglet.image.load(Path('sprites/blackjack_icon.png'))
    

        self.background_image = pyglet.image.load(Path('sprites/blackjack_background.jpg'))
        self.background = pyglet.sprite.Sprite(self.background_image, group=self.background_group)

        self.game = Game(
            batch = self.batch,
            group = self.cards
        )

    def on_mouse_press(self,x,y, button, modifiers):
        self.game.botao_comprar.clica(x,y)
        self.game.botao_parar.clica(x,y)

    
    def on_draw(self):
        self.background.draw()
        
        if self.game.is_over:
                self.game.draw_result()
                print(self.game.result)
        else:
            self.batch.draw()
            self.game.botao_comprar.draw()
            self.game.botao_parar.draw()
            
                
