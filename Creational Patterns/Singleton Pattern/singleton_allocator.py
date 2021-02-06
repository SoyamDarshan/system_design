'''

for some components it only makes sense to have one in the system
Example
- Database repository
- object factory
Its a problem because the initializer call is expensive
- we only do it once
- we provide everyone with the same instance
Want to prevent anyone creating additional copies
Need to take care of lazy initialization
Its a class which is instantiated only once
'''
import random


class Database:
    _instance = None

    def __init__(self):
        id = random.randint(1, 101)
        print("Loading a database from file", id)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        print("This was called first")
        return cls._instance


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 is d2)
