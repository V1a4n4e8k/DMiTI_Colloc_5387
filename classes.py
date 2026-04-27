class natural:
    def __init__(self, data: list):
        self.data = data.copy()

    @property
    def n(self):
        return len(self.data)


class integer:
    def __init__(self, sign: int, data: natural):
        self.sign = sign      # 0 = +, 1 = -
        self.data = data


class rational:
    def __init__(self, numerator: integer, denominator: natural):
        self.numerator = numerator
        self.denominator = denominator


class polynom:
    def __init__(self, coef: list):
        self.coef = coef.copy()

    @property
    def deg(self):
        return len(self.coef) - 1
