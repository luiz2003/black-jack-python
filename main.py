import pyglet

window = pyglet.window.Window(resizable=True, caption='Blackjack')

icon = pyglet.image.load('blackjack_icon.png')
window.set_icon(icon)

background = pyglet.image.load('blackjack_background.jpg')

@window.event

def on_draw():
    window.clear()
    background.blit(0, 0)

pyglet.app.run()