from typing import List
from copy import deepcopy

class natural:
    def __init__(self, data: list):
        self.data = data.copy()

    @property
    def n(self):
        return len(self.data)

    def __str__(self):
        return ''.join(map(str, self.data))


class integer:
    def __init__(self, sign: int, data: natural):
        self.sign = sign      # 0 = +, 1 = -
        self.data = data

    def __str__(self):
        sgn = '+' if self.sign == 0 else 1
        return sgn + ''.join(map(str, self.data.data))


class rational:
    def __init__(self, numerator: integer, denominator: natural):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        sgn = '+' if self.numerator.sign == 0 else 1
        return sgn + ''.join(map(str, self.numerator.data.data)) + '/' + ''.join(map(str, self.denominator.data))


class polynom:
    def __init__(self, coef: List[rational]):
        self.coef = deepcopy(coef)

    @property
    def deg(self):
        return len(self.coef) - 1

    def __str__(self):
        pass