# A component solely responsible for the wholesale(not piecewise) creation of objects
# Factory is a separate class filled with methods which allows creation of various types of objects
from enum import Enum

from math import cos, sin


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    '''
    This will keep on increasing with more number of systems
    '''

    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = b * sin(b)

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}\n'


class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        p = Point()
        p.x = x
        p.y = y
        return p

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p1 = PointFactory.new_cartesian_point(2, 3)
    p2 = PointFactory.new_polar_point(1, 2)
    print(p1, p2)
