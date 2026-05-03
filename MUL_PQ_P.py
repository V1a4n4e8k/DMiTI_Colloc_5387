"""
P-3
Умножение многочлена на рациональное число
"""


from copy import deepcopy

import classes as cls

from MUL_QQ_Q import MUL_QQ_Q


def MUL_PQ_P(a: cls.polynom, b: cls.rational):
    f = deepcopy(a)
    g = deepcopy(b)

    new_coef = []

    for x in f.coef:
        new_coef.append(MUL_QQ_Q(x, g))

    return cls.polynom(new_coef)