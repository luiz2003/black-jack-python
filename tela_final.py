import pyglet
from pathlib import Path

window = pyglet.window.Window(caption='Blackjack')

icon = pyglet.image.load(Path('sprites/blackjack_icon.png'))
window.set_icon(icon)

background_image = pyglet.image.load(Path('sprites/blackjack_background.jpg'))
background = pyglet.sprite.Sprite(background_image)

hasWon = True

if hasWon == True:
    label = pyglet.text.Label('Você ganhou!',
                          font_name='blackjack_font',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
else:
    label = pyglet.text.Label('Você perdeu...',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event

def on_draw():
    window.clear()
    background.draw()
    label.draw()

pyglet.app.run()