class Square:
    def __init__(self, side=0):
        self.side = side
        print(self.side)

    def __str__(self):
        return "{}".format(self.side)


def calculate_area(rc):
    return rc.width * rc.height


class SquareToRectangleAdapter:
    def __init__(self, square):
        self.square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side

    def __str__(self):
        return "{}, {}".format(self.width, self.height)


rc = SquareToRectangleAdapter(Square(10))
print(calculate_area(rc))
