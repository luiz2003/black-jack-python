import pyglet
from pathlib import Path

window = pyglet.window.Window(caption='Blackjack')

icon = pyglet.image.load(Path('sprites/blackjack_icon.png'))
window.set_icon(icon)

background_image = pyglet.image.load(Path('sprites/blackjack_background.jpg'))
background = pyglet.sprite.Sprite(background_image)

gameResult = 'dealer_estourou'

if gameResult == 'empate':
    label = pyglet.text.Label('Empatou',
                          font_name='blackjack_font',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
elif gameResult == 'player_valormaior':
    label = pyglet.text.Label('Seu valor foi maior!',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
elif gameResult == 'dealer_valormaior':
    label = pyglet.text.Label('O valor do dealer foi maior...',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
elif gameResult == 'player_estourou':
    label = pyglet.text.Label('Seu valor ultrapassou 21...',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
elif gameResult == 'dealer_estourou':
    label = pyglet.text.Label('O dealer ultrapassou 21!',
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