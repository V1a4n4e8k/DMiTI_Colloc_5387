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
        sgn = '+' if self.sign == 0 else '-'
        return sgn + ''.join(map(str, self.data.data))


class rational:
    def __init__(self, numerator: integer, denominator: natural):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        sgn = '+' if self.numerator.sign == 0 else '-'
        return sgn + ''.join(map(str, self.numerator.data.data)) + '/' + ''.join(map(str, self.denominator.data))


class polynom:
    def __init__(self, coef: List[rational]):
        self.coef = deepcopy(coef)

    @property
    def deg(self):
        return len(self.coef) - 1

    def __str__(self):
        parts = []

        for i, coef in enumerate(self.coef):
            power = self.deg - i

            sign = '-' if coef.numerator.sign == 1 else '+'

            num = ''.join(map(str, coef.numerator.data.data))
            den = ''.join(map(str, coef.denominator.data))

            # пропускаем нулевые коэффициенты
            if num == '0':
                continue

            # коэффициент
            if den == '1':
                coef_str = num
            else:
                coef_str = f'({num}/{den})'

            # убираем 1 перед x
            if coef_str == '1' and power != 0:
                coef_str = ''

            # переменная
            if power > 1:
                term = f'{coef_str}x^{power}'
            elif power == 1:
                term = f'{coef_str}x'
            else:
                term = f'{coef_str}'

            # знак
            if len(parts) == 0:
                if sign == '-':
                    parts.append('-' + term)
                else:
                    parts.append(term)
            else:
                parts.append(f' {sign} {term}')

        if len(parts) == 0:
            return '0'

        return ''.join(parts)