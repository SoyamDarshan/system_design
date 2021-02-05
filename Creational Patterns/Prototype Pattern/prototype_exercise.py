import copy

'''
Implement Line.deep_copy() to perform a deep copy of the given line object.
this method should return a copy of a Line that contains copies of its start/end points
'''


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        return copy.deepcopy(self)
