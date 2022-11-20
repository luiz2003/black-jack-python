import pyglet
import pyglet.shapes
from src.botoes.botao_main import Widget

numeros = ["0","1","2","3","4","5","6","7","8","9"]

class BotaoAjuda(Widget):
    def __init__(self, x, y, width, height, texto, func):
        super().__init__(x, y, width, height, texto)
        self.on_click = func

class BotaoSair(Widget):
    def __init__(self, x, y, width, height, texto, func):
        super().__init__(x, y, width, height, texto)
        self.on_click = func

class BotaoComecar(Widget):
    def __init__(self, x, y, width, height, texto, func):
        super().__init__(x, y, width, height, texto)
        self.on_click = func

class QuantiaInicial(Widget):
    def __init__(self, x, y, width, height, texto=""):
        super().__init__(x, y, width, height,texto)
        self.selecionado = False
        self.texto = texto
        self.moldura = pyglet.shapes.BorderedRectangle(x, y, width, height, color=(128,0,0), border_color=(255, 255, 255))
        self.linha = pyglet.shapes.Line(x, y + 5, x + width, y + 5)
        self.label = pyglet.text.Label(self.texto,
                font_name='Arial',
                font_size=32,
                anchor_x='center', anchor_y='center',
                x = self.x + self.width // 2,
                y = self.y + self.height // 2)
    def draw(self):
        if self.selecionado:
            self.moldura.draw()
        self.linha.draw()
        self.label.draw()
    def clica(self, x, y):
        self.selecionado = False
        super().clica(x, y)
    def on_click(self):
        self.selecionado = True
        self.label.text = "0"
        
    def digita(self, symbol):
        if not self.selecionado:
            return
        if symbol == "BACKSPACE":
            self.label.text = self.label.text[0:-1]
        if symbol in numeros:
            self.label.text += symbol
        else:
            print("Erro, digite apenas números !")

    def __repr__(self):
        return f"Input '{self.texto}'"