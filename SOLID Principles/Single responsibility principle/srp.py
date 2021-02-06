import os

'''
Single Responsibility Principle
If we have a class that class should have its primary responsibility
and should not take open additional responsibility
'''


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

    def load(self, filename):
        pass

    def low_from_web(self, uri):
        pass


j = Journal()
j.add_entry('I cried today.')
j.add_entry('I ate a bug.')
print(f'Journal entries:\n{j}')

file = os.path.dirname(os.path.realpath(__file__))
# file = r''
PersistenceManager.save_to_file(j, file + "\\journal.txt")
with open(file + "\\journal.txt") as fh:
    print(fh.read())
