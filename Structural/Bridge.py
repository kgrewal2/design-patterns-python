# Separates the implementation from its implementation-independent part


class DrawingAPIOne(object):
    def draw_circle(self, x, y, radius):
        print(x, y, radius, "API1")


class DrawingAPITwo(object):
    def draw_circle(self, x, y, radius):
        print(x, y, radius, "API2")


class Circle(object):
    def __init__(self, x, y, radius, API):
        self.x = x
        self.y = y
        self.radius = radius
        self.API = API

    def draw(self):
        self.API.draw_circle(self.x, self.y, self.radius)

    def scale(self, scale):
        self.radius *= scale


circle1 = Circle(1, 2, 3, DrawingAPIOne())
circle1.draw()
circle1.scale(1.5)
circle1.draw()
