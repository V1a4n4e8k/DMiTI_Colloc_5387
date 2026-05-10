"""
P-2
Вычитание многочленов
"""


from copy import deepcopy

import classes as cls

from SUB_QQ_Q import SUB_QQ_Q


def SUB_PP_P(a: cls.polynom, b: cls.polynom):
    f = deepcopy(a)
    g = deepcopy(b)

    f.coef.reverse()
    g.coef.reverse()

    new_coef = []

    zero = cls.rational(
        cls.integer(0, cls.natural([0])),
        cls.natural([1])
    )

    max_len = max(len(f.coef), len(g.coef))

    for i in range(max_len):
        coef_f = f.coef[i] if i < len(f.coef) else zero
        coef_g = g.coef[i] if i < len(g.coef) else zero

        new_coef.append(SUB_QQ_Q(coef_f, coef_g))

    new_coef.reverse()

    # удаление ведущих нулей
    while (
        len(new_coef) > 1
        and new_coef[0].numerator.data.n == 1
        and new_coef[0].numerator.data.data[0] == 0
    ):
        new_coef.pop(0)

    return cls.polynom(new_coef)