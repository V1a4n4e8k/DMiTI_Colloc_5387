from classes import *
from copy import deepcopy

def DER_P_P(p : polynom):
    arr = deepcopy(p.coef)
    new_deg = p.deg - 1
    arr.pop(0)
    res = polynom(arr)
    return res
"""
print(DER_P_P(polynom([rational(integer(1, natural([1,2,3,4])), natural([1,2,3,4]))]*2)).coef[0])
"""