import pyglet
import pyglet.shapes

class Widget:

    def __init__(self, x: int, y:int, width:int, height:int, texto: str) -> None:
        
        if not(isinstance(x, int) or isinstance(y,int)):
            raise ValueError("Invalid value for x or y")

                
        if not(isinstance(width, int) or isinstance(height,int)):
            raise ValueError("Invalid value for width or height")

            
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

    def contem_ponto(self, x: int, y:int) -> bool:

        if not(isinstance(x, int) or isinstance(y,int)):
            raise ValueError("Invalid value for x or y")       
        
        return x >= self.x and x <= self.x + self.width \
            and y >= self.y and y <= self.y + self.height

    def clica(self, x: int, y: int) -> None:
        if not(isinstance(x, int) or isinstance(y,int)):
            raise ValueError("Invalid value for x or y")

        if self.contem_ponto(x, y):
            self.on_click()
    
    def draw(self) -> None:
        self.moldura.draw()
        self.label.draw()

    def __repr__(self) -> str:
        return f"Botão '{self.texto}'"

class Botao(Widget):
    def __init__(self, x, y, width, height, texto, func):
        super().__init__(x, y, width, height, texto)
        self.on_click = func