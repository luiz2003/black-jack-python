import pyglet
from pathlib import Path
from src.game.game import Game

game = Game()

@game.window.event
def on_mouse_press(x,y, button, modifiers):
    game.on_mouse_press(x, y)

@game.window.event
def on_draw():
    game.on_draw()

pyglet.app.run()