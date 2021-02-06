# Connecting components together with abstractions
# A mechanism that decouples an interface (hiearchy) form an implementation (hierarchy)
# Example
# circle square
# vector raster

# VectorCircle VectorSquare RasterCircle RasterSquare
from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass

    def render_square(self, side):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle of radius {radius}")


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing pixel for a circle of radius {radius}")


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self): pass

    def resize(self, factor): pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        # super().draw()
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == "__main__":
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()

    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
