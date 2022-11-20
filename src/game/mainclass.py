import pyglet
from pathlib import Path
from src.game.game import Game


class MeuJogo(pyglet.window.Window):
    def __init__(self, width, height):
        super().__init__(width, height,
            caption="BlackJack")
    
        self.batch = pyglet.graphics.Batch()
        self.cards = pyglet.graphics.OrderedGroup(1)
        self.background_group = pyglet.graphics.OrderedGroup(0)

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
        self.clear()
        self.background.draw()
        
        if self.game.has_finished:
                self.game.draw_result()
                self.game.botao_recomecar.draw()
                self.game.botao_menu.draw()
                print(self.game.result)
        else:
            self.batch.draw()
            self.game.botao_comprar.draw()
            self.game.botao_parar.draw()
            
                
