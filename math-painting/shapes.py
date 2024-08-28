class Rectangle:
    """A rectangle shape that can be drawn on a canvas"""

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.y:self.y + self.height, self.x:self.x + self.width] = self.color

class Square:
    """A square shape that can be drawn on a canvas"""

    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, canvas):
        canvas.data[self.y:self.y + self.size, self.x:self.x + self.size] = self.color
