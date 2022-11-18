import pyglet
import pyglet.shapes

class Widget:

    def __init__(self, x, y, width, height, texto):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.texto = texto
        self.moldura = pyglet.shapes.BorderedRectangle(x, y, width, height, color=(128,0,0), border_color=(255, 255, 255))
        self.label = pyglet.text.Label(self.texto,
                font_name='Times New Roman',
                font_size=18,
                anchor_x='center', anchor_y='center',
                x = self.x + self.width // 2,
                y = self.y + self.height // 2)

    def contem_ponto(self, x, y):
        return x >= self.x and x <= self.x + self.width \
            and y >= self.y and y <= self.y + self.height

    def clica(self, x, y):
        if self.contem_ponto(x, y):
            self.on_click()
    
    def draw(self):
        self.moldura.draw()
        self.label.draw()

    def __repr__(self):
        return f"Botão '{self.texto}'"

class BotaoRecomecar(Widget):
    def __init__(self, x, y, width, height, texto, func):
        super().__init__(x, y, width, height, texto)
        self.on_click = func

class BotaoMenu(Widget):
    def __init__(self, x, y, width, height, texto, func):
        super().__init__(x, y, width, height, texto)
        self.on_click = func

class BotaoComprar(Widget):
    def __init__(self, x, y, width, height, texto, func):
        super().__init__(x, y, width, height, texto)
        self.on_click = func

class BotaoParar(Widget):
    def __init__(self, x, y, width, height, texto, func):
        super().__init__(x, y, width, height, texto)
        self.on_click = func