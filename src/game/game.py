from ..cartas import baralho
from ..dealer import dealer
from ..player import player
from ..botoes.botao_main import Botao
from ..apostas import apostas
import pyglet
from pathlib import Path


class Game(pyglet.window.Window):

    def __init__(self) -> None:
        super().__init__(caption="Blackjack")

        self.batch = pyglet.graphics.Batch()
        self.card_group = pyglet.graphics.OrderedGroup(1)
        self.background_group = pyglet.graphics.OrderedGroup(0)

        self.icon = pyglet.image.load(Path('sprites/blackjack_icon.png'))
        self.set_icon(self.icon)

        self.background_image = pyglet.image.load(Path('sprites/blackjack_background.jpg'))
        self.background = pyglet.sprite.Sprite(self.background_image, group=self.background_group)

        self._stop = False

        self.deck = baralho.Baralho()

        self.dealer = dealer.Dealer()

        self.player = player.Player()

        self.dealer.start_game(self.player)

        self.define_positions()

        self.dealer_sprite_group = pyglet.graphics.OrderedGroup(2, parent=self.card_group)

        back_image = pyglet.image.load(Path('./sprites/CartaVirada.png').resolve())
        self.back_image_sprite = pyglet.sprite.Sprite(back_image, batch=self.batch, group=self.card_group, x=50,
                                                      y=self._height - 100)
        self.dealer.hand[0].sprite.batch = self.batch
        self.dealer.hand[0].sprite.group = self.dealer_sprite_group
        self.dealer.hand[0].sprite.position = (self.back_image_sprite.width + 70, self._height - 100)

        self.botao_comprar = Botao(20, 50, 100, 50, "Comprar", self.buy_card)
        self.botao_parar = Botao(520, 50, 100, 50, "Parar", self.on_click_stop)
        self.botao_menu = Botao(470, 50, 150, 50, "Ir para Menu", self.go_to_menu)

        self.botao_apostas = apostas.Aposta(470, 400, 150, 50, "Apostar")

        self.result = ""

    @property
    def has_finished(self) -> bool:
        player_total_value = self.player.total_value
        dealer_total_value = self.dealer.total_value

        if player_total_value > 21 and dealer_total_value > 21:
            self.result = "empate"
            return True
        elif player_total_value > 21:
            self.result = "player_estourou"
            return True
        elif self._stop and player_total_value > dealer_total_value:
            self.result = "player_valormaior"
            return True
        elif self._stop:
            self.result = "dealer_valormaior"
            return True

    def draw_result(self) -> None:
        if self.result == 'empate':
            label = pyglet.text.Label('Empatou',
                                      font_name='blackjack_font',
                                      font_size=36,
                                      x=self._width // 2, y=self._height // 2,
                                      anchor_x='center', anchor_y='center')
            if self.valor != "Apostar":
                label1 = pyglet.text.Label(f'Você ganhou suas fichas de volta!',
                                           font_name='Times New Roman',
                                           font_size=30,
                                           x=self._width // 2, y=150,
                                           anchor_x='center', anchor_y='center')
        elif self.result == 'player_valormaior':
            label = pyglet.text.Label('Seu valor foi maior!',
                                      font_name='Times New Roman',
                                      font_size=36,
                                      x=self._width // 2, y=self._height // 2,
                                      anchor_x='center', anchor_y='center')
            if self.valor != "Apostar":
                label1 = pyglet.text.Label(f'Você ganhou {int(self.valor) * 2} fichas!',
                                           font_name='Times New Roman',
                                           font_size=30,
                                           x=self._width // 2, y=150,
                                           anchor_x='center', anchor_y='center')
        elif self.result == 'dealer_valormaior':
            label = pyglet.text.Label('O valor do dealer foi maior...',
                                      font_name='Times New Roman',
                                      font_size=36,
                                      x=self._width // 2, y=self._height // 2,
                                      anchor_x='center', anchor_y='center')
            if self.valor != "Apostar":
                label1 = pyglet.text.Label(f'Você perdeu {self.valor} fichas...',
                                           font_name='Times New Roman',
                                           font_size=30,
                                           x=self._width // 2, y=150,
                                           anchor_x='center', anchor_y='center')
        elif self.result == 'player_estourou':
            label = pyglet.text.Label('Seu valor ultrapassou 21...',
                                      font_name='Times New Roman',
                                      font_size=36,
                                      x=self._width // 2, y=self._height // 2,
                                      anchor_x='center', anchor_y='center')
            if self.valor != "Apostar":
                label1 = pyglet.text.Label(f'Você perdeu {self.valor} fichas...',
                                           font_name='Times New Roman',
                                           font_size=30,
                                           x=self._width // 2, y=150,
                                           anchor_x='center', anchor_y='center')
        elif self.result == 'dealer_estourou':
            label = pyglet.text.Label('O dealer ultrapassou 21!',
                                      font_name='Times New Roman',
                                      font_size=36,
                                      x=self._width // 2, y=self._height // 2,
                                      anchor_x='center', anchor_y='center')
            if self.valor != "Apostar":
                label1 = pyglet.text.Label(f'Você ganhou {int(self.valor) * 2} fichas!',
                                           font_name='Times New Roman',
                                           font_size=30,
                                           x=self._width // 2, y=150,
                                           anchor_x='center', anchor_y='center')
        elif player.hasBlackJack == True:
            if self.valor != "Apostar":
                label1 = pyglet.text.Label(f'Você ganhou {int(self.valor) * 3} fichas!',
                                               font_name='Times New Roman',
                                               font_size=30,
                                               x=self._width // 2, y=150,
                                               anchor_x='center', anchor_y='center')
        label.draw()
        
        if self.valor != "Apostar":
            label1.draw()

    def buy_card(self) -> None:
        self.dealer.pull_card(self.player)
        self.define_positions()
        self.valor = self.botao_apostas.label.text

    def on_click_stop(self) -> None:
        self._stop = True
        self.valor = self.botao_apostas.label.text

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if self.has_finished:
            self.botao_menu.clica(x, y)
        else:
            self.botao_comprar.clica(x, y)
            self.botao_parar.clica(x, y)
            self.botao_apostas.clica(x, y)

    def on_text(self, text):
        self.botao_apostas.digita(text)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.BACKSPACE:
            self.botao_apostas.digita("BACKSPACE")

    def on_draw(self) -> None:
        self.clear()
        self.background.draw()

        if self.has_finished:
            self.draw_result()
            self.botao_menu.draw()
            print()

        else:
            self.batch.draw()
            self.botao_comprar.draw()
            self.botao_parar.draw()
            self.botao_apostas.draw()

    def go_to_menu(self):
        self.close()

    def define_positions(self) -> None:
        player_total_width = 0

        for card in self.player.hand:
            player_total_width += card.sprite.width

        player_total_width += len(self.player.hand) * 25

        x = 0
        for card in self.player.hand:
            card.sprite.batch = self.batch
            card.sprite.group = self.card_group
            card.sprite.position = (self._width // 2 - player_total_width // 2 + x * 30 + x * card.sprite.width, 50)
            x += 1
