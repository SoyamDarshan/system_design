class Circle:
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return 'A circle of radius {}'.format(self.radius)


class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return 'A square with side {}'.format(self.side)


class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        # todo
        # note that a Square doesn't have resize()
        if isinstance(self.shape, Circle):
            self.shape.radius *= factor

    def __str__(self):
        return '{} has the color {}'.format(self.shape, self.color)
