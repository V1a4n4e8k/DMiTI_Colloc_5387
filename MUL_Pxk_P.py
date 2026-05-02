"""
P-4
Умножение многочлена на x^k, k-натуральное или 0
"""

from classes import *
from copy import deepcopy

# Доделайте rational чтобы эту функцию тоже можно было сделать.
def MUL_Pxk_P(a : polynom, k : natural):
    res = deepcopy(a)
    for i in range(k):
        res.coef.append(0)
    return res
"""
print(MUL_Pxk_P(polynom([rational(integer(1, natural([1,2,3,4])), natural([1,2,3,4]))]*2), 3).deg)
"""