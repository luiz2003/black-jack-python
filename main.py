import pyglet

window = pyglet.window.Window(caption='Blackjack')

batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
cards = pyglet.graphics.OrderedGroup(1)

icon = pyglet.image.load('blackjack_icon.png')
window.set_icon(icon)

background_image = pyglet.image.load('blackjack_background.jpg')
background = pyglet.sprite.Sprite(background_image, batch=batch, group=background)

AEspadas_image = pyglet.image.load('AEspadas.png')
AEspadas = pyglet.sprite.Sprite(AEspadas_image, batch=batch, group=cards, x=10, y=200)

DoisEspadas_image = pyglet.image.load('2Espadas.png')
DoisEspadas = pyglet.sprite.Sprite(DoisEspadas_image, batch=batch, group=cards, x=50, y=200)

TresEspadas_image = pyglet.image.load('3Espadas.png')
TresEspadas = pyglet.sprite.Sprite(TresEspadas_image, batch=batch, group=cards, x=90, y=200)

QuatroEspadas_image = pyglet.image.load('4Espadas.png')
QuatroEspadas = pyglet.sprite.Sprite(QuatroEspadas_image, batch=batch, group=cards, x=130, y=200)

CincoEspadas_image = pyglet.image.load('5Espadas.png')
CincoEspadas = pyglet.sprite.Sprite(CincoEspadas_image, batch=batch, group=cards, x=170, y=200)

SeisEspadas_image = pyglet.image.load('6Espadas.png')
SeisEspadas = pyglet.sprite.Sprite(SeisEspadas_image, batch=batch, group=cards, x=210, y=200)

SeteEspadas_image = pyglet.image.load('7Espadas.png')
SeteEspadas = pyglet.sprite.Sprite(SeteEspadas_image, batch=batch, group=cards, x=250, y=200)

OitoEspadas_image = pyglet.image.load('8Espadas.png')
OitoEspadas = pyglet.sprite.Sprite(OitoEspadas_image, batch=batch, group=cards, x=290, y=200)

NoveEspadas_image = pyglet.image.load('9Espadas.png')
NoveEspadas = pyglet.sprite.Sprite(NoveEspadas_image, batch=batch, group=cards, x=330, y=200)

DezEspadas_image = pyglet.image.load('10Espadas.png')
DezEspadas = pyglet.sprite.Sprite(DezEspadas_image, batch=batch, group=cards, x=370, y=200)

ValeteEspadas_image = pyglet.image.load('ValeteEspadas.png')
ValeteEspadas = pyglet.sprite.Sprite(ValeteEspadas_image, batch=batch, group=cards, x=410, y=200)

RainhaEspadas_image = pyglet.image.load('RainhaEspadas.png')
RainhaEspadas = pyglet.sprite.Sprite(RainhaEspadas_image, batch=batch, group=cards, x=450, y=200)

ReiEspadas_image = pyglet.image.load('ReiEspadas.png')
ReiEspadas = pyglet.sprite.Sprite(ReiEspadas_image, batch=batch, group=cards, x=490, y=200)

@window.event

def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()