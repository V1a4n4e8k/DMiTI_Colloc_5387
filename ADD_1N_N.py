"""
N-3
Добавление 1 к натуральному числу
"""

import classes
from classes import natural


def ADD_1N_N(a: classes.natural):
    res = a.data.copy()
    i = len(res) - 1

    while i >= 0:
        if res[i] < 9:
            res[i] += 1
            return classes.natural(res)

    res[i] = 0
    i -= 1

    return classes.natural([1] + [0] * i)

