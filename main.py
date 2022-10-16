import pyglet
from pathlib import Path
from src.game.game import Game
from botoes_main import BotaoComprar, BotaoParar

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

botao_comprar = BotaoComprar(20, 50, 100, 50, "Comprar")
botao_parar = BotaoParar(520, 50, 100, 50, "Parar")

@window.event

def on_draw():
    window.clear()
    background.draw()
    batch.draw()
    botao_comprar.draw()
    botao_parar.draw()

pyglet.app.run()