"""
N-4
Сложение натуральных чисел
"""

import classes
from classes import natural


def ADD_NN_N(a: classes.natural, b: classes.natural):
    i = a.n - 1
    j = b.n - 1
    ost = 0
    res = []

    while i >= 0 or j >= 0 or ost > 0:
        dig_a = a.data[i] if i >= 0 else 0
        dig_b = b.data[j] if j >= 0 else 0

        s = dig_a + dig_b + ost
        res.append(s % 10)
        ost = s // 10

        i -= 1
        j -= 1

    res.reverse()
    return classes.natural(res)

