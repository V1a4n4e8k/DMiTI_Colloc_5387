"""
P-1
Сложение многочленов
"""


from copy import deepcopy

import classes as cls

from ADD_QQ_Q import ADD_QQ_Q


def ADD_PP_P(a: cls.polynom, b: cls.polynom):
    f = deepcopy(a)
    g = deepcopy(b)

    f.coef.reverse()
    g.coef.reverse()

    new_coef = []

    for i, x in enumerate(g.coef):
        if i > f.deg:
            new_coef.append(x)
        else:
            new_coef.append(ADD_QQ_Q(f.coef[i], x))

    new_coef.reverse()

    return cls.polynom(new_coef)