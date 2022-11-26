import pyglet
from src.menu.menu import MeuMenu
from pathlib import Path

jogo = MeuMenu(929,626)
icon = pyglet.image.load(Path('sprites/blackjack_icon.png'))
jogo.set_icon(icon)

pyglet.app.run()