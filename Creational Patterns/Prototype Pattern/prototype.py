# Reiterate existing designs
# An existing (partially or fully constructed) design is a Prototype
# We make a copy (clone) the prototype and customize it (Requires deep copy support)
# A partially or fully initialized object that we copy (clone) and make use of it.
import copy


class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


# Fact: Shallow Copy any copy of a reference will not get copied
address = Address('123 London Road', 'London', 'UK')
john = Person('John', address)
print(john)
jane = copy.deepcopy(john)
jane.address.street_address = '124 London Road'
jane.name = 'Jane'
print(john)
print(jane)
