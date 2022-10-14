import pyglet
from pathlib import Path
from src.game.game import Game

window = pyglet.window.Window(caption='Blackjack')

batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
cards = pyglet.graphics.OrderedGroup(1)

icon = pyglet.image.load(Path('sprites/blackjack_icon.png'))
window.set_icon(icon)


background_image = pyglet.image.load(Path('sprites/blackjack_background.jpg'))
background = pyglet.sprite.Sprite(background_image)

game = Game(
    batch = batch,
    group = cards
)

@window.event

def on_draw():
    window.clear()
    background.draw()
    batch.draw()

pyglet.app.run()