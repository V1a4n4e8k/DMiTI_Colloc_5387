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

    max_len = max(len(f.coef), len(g.coef))

    zero = cls.rational(
        cls.integer(0, cls.natural([0])),
        cls.natural([1])
    )

    for i in range(max_len):
        coef_f = f.coef[i] if i < len(f.coef) else zero
        coef_g = g.coef[i] if i < len(g.coef) else zero

        new_coef.append(ADD_QQ_Q(coef_f, coef_g))

    new_coef.reverse()

    return cls.polynom(new_coef)