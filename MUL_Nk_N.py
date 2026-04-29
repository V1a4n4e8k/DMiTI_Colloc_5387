"""
N-7
Умножение натурального числа на 10^k, k-натуральное (не длинное)
"""

import classes

def MUL_Nk_N(a: classes.natural, k: int):
    if a.n == 1 and a.data[0] == 0:
        return classes.natural([0])

    res = a.data.copy()

    for i in range(k):
        res.append(0)

    return classes.natural(res)