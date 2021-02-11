"""
A component that processes structured text data. Does so by turning it into separated lexical tokens(lexing)
and the interpreting the sequences of said tokens (parsing)

"""
# Lexing
from enum import Enum, auto


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPAREN = auto()
        RPAREN = auto()

    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __str__(self):
        return f'`{self.text}`'


def lex(data):
    result = []
    i = 0
    while i < len(data):
        if data[i] == '+':
            result.append(Token(Token.Type.PLUS, '+'))
        elif data[i] == '-':
            result.append(Token(Token.Type.MINUS, '-'))
        elif data[i] == '(':
            result.append(Token(Token.Type.LPAREN, '('))
        elif data[i] == ')':
            result.append(Token(Token.Type.RPAREN, ')'))
        else:
            digits = [data[i]]
            for j in range(i + 1, len(data)):
                if data[j].isdigit():
                    digits.append(data[j])
                    i += 1
                else:
                    result.append(Token(Token.Type.INTEGER, ''.join(digits)))
                    break
        i += 1
    return result


def calc(data):
    tokens = lex(data)
    print(' '.join(map(str, tokens)))


if __name__ == '__main__':
    calc('(13+4)-(12+1)')
