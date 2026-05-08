"""
P-4
Умножение многочлена на x^k, k-натуральное или 0
"""

import classes as cl
from copy import deepcopy

# Доделайте rational чтобы эту функцию тоже можно было сделать.
def MUL_Pxk_P(a : cl.polynom, k : int):
    res = deepcopy(a)
    for i in range(k):
        res.coef.append(cl.rational(cl.integer(0,cl.natural([0])),cl.natural([1])))
    return res
"""
print(MUL_Pxk_P(polynom([rational(integer(1, natural([1,2,3,4])), natural([1,2,3,4]))]*2), 3).deg)
"""