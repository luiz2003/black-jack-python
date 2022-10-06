import pyglet
from pathlib import Path
import cards

window = pyglet.window.Window(caption='Blackjack')

icon = pyglet.image.load(Path('sprites/blackjack_icon.png'))
window.set_icon(icon)

background_image = pyglet.image.load(Path('sprites/blackjack_background.jpg'))
background = pyglet.sprite.Sprite(background_image)

cards.AEspadas.update(x=300, y=200)

@window.event

def on_draw():
    window.clear()
    background.draw()
    cards.AEspadas.draw()

pyglet.app.run()