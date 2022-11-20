import pyglet
from pathlib import Path
from src.game.game import Game

batch = pyglet.graphics.Batch()
cards = pyglet.graphics.OrderedGroup(1)
background_group = pyglet.graphics.OrderedGroup(0)

window = pyglet.window.Window(caption='Blackjack')

icon = pyglet.image.load(Path('sprites/blackjack_icon.png'))
window.set_icon(icon)

background_image = pyglet.image.load(Path('sprites/blackjack_background.jpg'))
background = pyglet.sprite.Sprite(background_image, group=background_group)

game = Game(
    batch = batch,
    group = cards
)

@window.event
def on_mouse_press(x,y, button, modifiers):
    game.botao_comprar.clica(x,y)
    game.botao_parar.clica(x,y)

@window.event
def on_draw():
    window.clear()
    background.draw()
    
    if game.has_finished:
        game.draw_result()
        game.botao_recomecar.draw()
        game.botao_menu.draw()
        print(game.result)
          
    else:
        batch.draw()
        game.botao_comprar.draw()
        game.botao_parar.draw()

pyglet.app.run()