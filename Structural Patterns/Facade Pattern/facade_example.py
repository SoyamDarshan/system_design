from random import randint


class Generator:
    def generate(self, count):
        return [randint(1, 9) for x in range(count)]


class Splitter:
    def split(self, array):
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:
    def verify(self, arrays):
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:
    def generate(self, size):
        # todo - return a magic square of the given size
        verify = Verifier()
        arr = Generator()
        splitter = Splitter()

        new_matrix = [arr.generate(size) for i in range(size)]
        split_matrix = splitter.split(new_matrix)

        while not verify.verify(split_matrix):
            new_matrix = [arr.generate(size) for i in range(size)]
            split_matrix = splitter.split(new_matrix)
            print(split_matrix)
        return new_matrix


if __name__ == "__main__":
    """
    Magic square is a square where:
    - sum of all rows is equal
    - sum of all columns is equal
    - sum of all diagonals is equal
    """
    msg = MagicSquareGenerator()
    print(msg.generate(3))
