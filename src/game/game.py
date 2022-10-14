from ..cartas import baralho
from ..dealer import dealer
from ..player import player
import pyglet
from pathlib import Path

class Game :
    def __init__(self, batch , group, window_width = 640, window_heigth = 480 ):

        self.batch =  batch
        self.card_group = group
        self.window_width = window_width
        self.window_heigth = window_heigth

        self.deck = baralho.Baralho()

        self.dealer = dealer.Dealer()

        self.player = player.Player()

        self.dealer.start_game(self.player) 

        self.define_positions()

        self.dealer_sprite_group = pyglet.graphics.OrderedGroup(2)

        back_image =  pyglet.image.load(Path('./sprites/CartaVirada.png').resolve())
        self.back_image_sprite = pyglet.sprite.Sprite(back_image, batch=self.batch, group=self.card_group, x= 50, y= self.window_heigth - 100 )
        self.dealer.hand[0].sprite.batch = self.batch
        self.dealer.hand[0].sprite.group = self.dealer_sprite_group
        self.dealer.hand[0].sprite.position = (self.back_image_sprite.width + 25, self.window_heigth - 100)
        
    def define_positions(self):
        player_total_width = 0

        for card in self.player.hand:
            player_total_width += card.sprite.width

        player_total_width += len(self.player.hand) * 25

        x = 0
        for card in self.player.hand:
            card.sprite.batch = self.batch
            card.sprite.group = self.card_group
            card.sprite.position = (self.window_width//2 - player_total_width//2 + x*30 + x*card.sprite.width, 50)
            x+=1
        

