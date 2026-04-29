"""
N-6
Умножение натурального числа на цифру
"""

import classes
from classes import natural


def MUL_ND_N(a: classes.natural, n: int):
    if n == 0:
        return classes.natural([0])

    if n == 1:
        return classes.natural(a.data)

    res = []
    ost = 0
    i = a.n - 1

    while i >= 0 or ost > 0:
        dig = a.data[i] if i >= 0 else 0

        val = dig * n + ost
        res.append(val % 10)
        ost = val // 10

        i -= 1

    res.reverse()
    return classes.natural(res)
