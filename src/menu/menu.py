from ..botoes.botoes_main import Botao

class Menu:
    def __init__(self, batch, window_width = 640, window_height = 480):
        self.batch =  batch
        self.window_width = window_width
        self.window_height = window_height

        self.botao_comecar = Botao(20, 50, 100, 50, "Começar", self.start_game)
        self.botao_apostar = Botao(520, 50, 100, 50, "Apostar", self.do_bet)
        
        self.result = ""

    def start_game(self):
        pass

    def do_bet(self):
        pass
