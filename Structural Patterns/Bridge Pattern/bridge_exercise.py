class Shape:
    def __init__(self, renderer):
        self.name = None
        self.renderer = renderer


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Triangle'

    def __str__(self):
        return str(self.renderer).format(self.name)


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Square'

    def __str__(self):
        return str(self.renderer).format(self.name)


#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too
from abc import ABC


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer
class VectorRenderer(Renderer):
    def __str__(self):
        return 'Drawing {} as lines'


class RasterRenderer(Renderer):
    def __str__(self):
        return 'Drawing {} as pixels'
