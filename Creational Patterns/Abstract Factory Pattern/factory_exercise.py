class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    def __init__(self):
        self._id = 0

    def create_person(self, name):
        p = Person(name=name, id=self._id)
        self._id += 1
        return p
