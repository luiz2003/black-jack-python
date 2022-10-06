import pyglet
from pathlib import Path

batch = pyglet.graphics.Batch()

cards_sprites = []

AEspadas_image = pyglet.image.load(Path('sprites/AEspadas.png'))
AEspadas = pyglet.sprite.Sprite(AEspadas_image, batch=batch)
cards_sprites.append(AEspadas)

DoisEspadas_image = pyglet.image.load(Path('sprites/2Espadas.png'))
DoisEspadas = pyglet.sprite.Sprite(DoisEspadas_image, batch=batch)
cards_sprites.append(DoisEspadas)

TresEspadas_image = pyglet.image.load(Path('sprites/3Espadas.png'))
TresEspadas = pyglet.sprite.Sprite(TresEspadas_image, batch=batch)
cards_sprites.append(TresEspadas)

QuatroEspadas_image = pyglet.image.load(Path('sprites/4Espadas.png'))
QuatroEspadas = pyglet.sprite.Sprite(QuatroEspadas_image, batch=batch)
cards_sprites.append(QuatroEspadas)

CincoEspadas_image = pyglet.image.load(Path('sprites/5Espadas.png'))
CincoEspadas = pyglet.sprite.Sprite(CincoEspadas_image, batch=batch)
cards_sprites.append(CincoEspadas)

SeisEspadas_image = pyglet.image.load(Path('sprites/6Espadas.png'))
SeisEspadas = pyglet.sprite.Sprite(SeisEspadas_image, batch=batch)
cards_sprites.append(SeisEspadas)

SeteEspadas_image = pyglet.image.load(Path('sprites/7Espadas.png'))
SeteEspadas = pyglet.sprite.Sprite(SeteEspadas_image, batch=batch)
cards_sprites.append(SeteEspadas)

OitoEspadas_image = pyglet.image.load(Path('sprites/8Espadas.png'))
OitoEspadas = pyglet.sprite.Sprite(OitoEspadas_image, batch=batch)
cards_sprites.append(OitoEspadas)

NoveEspadas_image = pyglet.image.load(Path('sprites/9Espadas.png'))
NoveEspadas = pyglet.sprite.Sprite(NoveEspadas_image, batch=batch)
cards_sprites.append(NoveEspadas)

DezEspadas_image = pyglet.image.load(Path('sprites/10Espadas.png'))
DezEspadas = pyglet.sprite.Sprite(DezEspadas_image, batch=batch)
cards_sprites.append(DezEspadas)

ValeteEspadas_image = pyglet.image.load(Path('sprites/ValeteEspadas.png'))
ValeteEspadas = pyglet.sprite.Sprite(ValeteEspadas_image, batch=batch)
cards_sprites.append(ValeteEspadas)

RainhaEspadas_image = pyglet.image.load(Path('sprites/RainhaEspadas.png'))
RainhaEspadas = pyglet.sprite.Sprite(RainhaEspadas_image, batch=batch)
cards_sprites.append(RainhaEspadas)

ReiEspadas_image = pyglet.image.load(Path('sprites/ReiEspadas.png'))
ReiEspadas = pyglet.sprite.Sprite(ReiEspadas_image, batch=batch)
cards_sprites.append(ReiEspadas)

APaus_image = pyglet.image.load(Path('sprites/APaus.png'))
APaus = pyglet.sprite.Sprite(APaus_image, batch=batch)
cards_sprites.append(APaus)

DoisPaus_image = pyglet.image.load(Path('sprites/2Paus.png'))
DoisPaus = pyglet.sprite.Sprite(DoisPaus_image, batch=batch)
cards_sprites.append(DoisPaus)

TresPaus_image = pyglet.image.load(Path('sprites/3Paus.png'))
TresPaus = pyglet.sprite.Sprite(TresPaus_image, batch=batch)
cards_sprites.append(TresPaus)

QuatroPaus_image = pyglet.image.load(Path('sprites/4Paus.png'))
QuatroPaus = pyglet.sprite.Sprite(QuatroPaus_image, batch=batch)
cards_sprites.append(QuatroPaus)

CincoPaus_image = pyglet.image.load(Path('sprites/5Paus.png'))
CincoPaus = pyglet.sprite.Sprite(CincoPaus_image, batch=batch)
cards_sprites.append(CincoPaus)

SeisPaus_image = pyglet.image.load(Path('sprites/6Paus.png'))
SeisPaus = pyglet.sprite.Sprite(SeisPaus_image, batch=batch)
cards_sprites.append(SeisPaus)

SetePaus_image = pyglet.image.load(Path('sprites/7Paus.png'))
SetePaus = pyglet.sprite.Sprite(SetePaus_image, batch=batch)
cards_sprites.append(SetePaus)

OitoPaus_image = pyglet.image.load(Path('sprites/8Paus.png'))
OitoPaus = pyglet.sprite.Sprite(OitoPaus_image, batch=batch)
cards_sprites.append(OitoPaus)

NovePaus_image = pyglet.image.load(Path('sprites/9Paus.png'))
NovePaus = pyglet.sprite.Sprite(NovePaus_image, batch=batch)
cards_sprites.append(NovePaus)

DezPaus_image = pyglet.image.load(Path('sprites/10Paus.png'))
DezPaus = pyglet.sprite.Sprite(DezPaus_image, batch=batch)
cards_sprites.append(DezPaus)

ValetePaus_image = pyglet.image.load(Path('sprites/ValetePaus.png'))
ValetePaus = pyglet.sprite.Sprite(ValetePaus_image, batch=batch)
cards_sprites.append(ValetePaus)

RainhaPaus_image = pyglet.image.load(Path('sprites/RainhaPaus.png'))
RainhaPaus = pyglet.sprite.Sprite(RainhaPaus_image, batch=batch)
cards_sprites.append(RainhaPaus)

ReiPaus_image = pyglet.image.load(Path('sprites/ReiPaus.png'))
ReiPaus = pyglet.sprite.Sprite(ReiPaus_image, batch=batch)
cards_sprites.append(ReiPaus)

ACopas_image = pyglet.image.load(Path('sprites/ACopas.png'))
ACopas = pyglet.sprite.Sprite(ACopas_image, batch=batch)
cards_sprites.append(ACopas)

DoisCopas_image = pyglet.image.load(Path('sprites/2Copas.png'))
DoisCopas = pyglet.sprite.Sprite(DoisCopas_image, batch=batch)
cards_sprites.append(DoisCopas)

TresCopas_image = pyglet.image.load(Path('sprites/3Copas.png'))
TresCopas = pyglet.sprite.Sprite(TresCopas_image, batch=batch)
cards_sprites.append(TresCopas)

QuatroCopas_image = pyglet.image.load(Path('sprites/4Copas.png'))
QuatroCopas = pyglet.sprite.Sprite(QuatroCopas_image, batch=batch)
cards_sprites.append(QuatroCopas)

CincoCopas_image = pyglet.image.load(Path('sprites/5Copas.png'))
CincoCopas = pyglet.sprite.Sprite(CincoCopas_image, batch=batch)
cards_sprites.append(CincoCopas)

SeisCopas_image = pyglet.image.load(Path('sprites/6Copas.png'))
SeisCopas = pyglet.sprite.Sprite(SeisCopas_image, batch=batch)
cards_sprites.append(SeisCopas)

SeteCopas_image = pyglet.image.load(Path('sprites/7Copas.png'))
SeteCopas = pyglet.sprite.Sprite(SeteCopas_image, batch=batch)
cards_sprites.append(SeteCopas)

OitoCopas_image = pyglet.image.load(Path('sprites/8Copas.png'))
OitoCopas = pyglet.sprite.Sprite(OitoCopas_image, batch=batch)
cards_sprites.append(OitoCopas)

NoveCopas_image = pyglet.image.load(Path('sprites/9Copas.png'))
NoveCopas = pyglet.sprite.Sprite(NoveCopas_image, batch=batch)
cards_sprites.append(NoveCopas)

DezCopas_image = pyglet.image.load(Path('sprites/10Copas.png'))
DezCopas = pyglet.sprite.Sprite(DezCopas_image, batch=batch)
cards_sprites.append(DezCopas)

ValeteCopas_image = pyglet.image.load(Path('sprites/ValeteCopas.png'))
ValeteCopas = pyglet.sprite.Sprite(ValeteCopas_image, batch=batch)
cards_sprites.append(ValeteCopas)

RainhaCopas_image = pyglet.image.load(Path('sprites/RainhaCopas.png'))
RainhaCopas = pyglet.sprite.Sprite(RainhaCopas_image, batch=batch)
cards_sprites.append(RainhaCopas)

ReiCopas_image = pyglet.image.load(Path('sprites/ReiCopas.png'))
ReiCopas = pyglet.sprite.Sprite(ReiCopas_image, batch=batch)
cards_sprites.append(ReiCopas)

AOuro_image = pyglet.image.load(Path('sprites/AOuro.png'))
AOuro = pyglet.sprite.Sprite(AOuro_image, batch=batch)
cards_sprites.append(AOuro)

DoisOuro_image = pyglet.image.load(Path('sprites/2Ouro.png'))
DoisOuro = pyglet.sprite.Sprite(DoisOuro_image, batch=batch)
cards_sprites.append(DoisOuro)

TresOuro_image = pyglet.image.load(Path('sprites/3Ouro.png'))
TresOuro = pyglet.sprite.Sprite(TresOuro_image, batch=batch)
cards_sprites.append(TresOuro)

QuatroOuro_image = pyglet.image.load(Path('sprites/4Ouro.png'))
QuatroOuro = pyglet.sprite.Sprite(QuatroOuro_image, batch=batch)
cards_sprites.append(QuatroOuro)

CincoOuro_image = pyglet.image.load(Path('sprites/5Ouro.png'))
CincoOuro = pyglet.sprite.Sprite(CincoOuro_image, batch=batch)
cards_sprites.append(CincoOuro)

SeisOuro_image = pyglet.image.load(Path('sprites/6Ouro.png'))
SeisOuro = pyglet.sprite.Sprite(SeisOuro_image, batch=batch)
cards_sprites.append(SeisOuro)

SeteOuro_image = pyglet.image.load(Path('sprites/7Ouro.png'))
SeteOuro = pyglet.sprite.Sprite(SeteOuro_image, batch=batch)
cards_sprites.append(SeteOuro)

OitoOuro_image = pyglet.image.load(Path('sprites/8Ouro.png'))
OitoOuro = pyglet.sprite.Sprite(OitoOuro_image, batch=batch)
cards_sprites.append(OitoOuro)

NoveOuro_image = pyglet.image.load(Path('sprites/9Ouro.png'))
NoveOuro = pyglet.sprite.Sprite(NoveOuro_image, batch=batch)
cards_sprites.append(NoveOuro)

DezOuro_image = pyglet.image.load(Path('sprites/10Ouro.png'))
DezOuro = pyglet.sprite.Sprite(DezOuro_image, batch=batch)
cards_sprites.append(DezOuro)

ValeteOuro_image = pyglet.image.load(Path('sprites/ValeteOuro.png'))
ValeteOuro = pyglet.sprite.Sprite(ValeteOuro_image, batch=batch)
cards_sprites.append(ValeteOuro)

RainhaOuro_image = pyglet.image.load(Path('sprites/RainhaOuro.png'))
RainhaOuro = pyglet.sprite.Sprite(RainhaOuro_image, batch=batch)
cards_sprites.append(RainhaOuro)

ReiOuro_image = pyglet.image.load(Path('sprites/ReiOuro.png'))
ReiOuro = pyglet.sprite.Sprite(ReiOuro_image, batch=batch)
cards_sprites.append(ReiOuro)