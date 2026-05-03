"""
P-2
Вычитание многочленов
"""


from copy import deepcopy

import classes as cls

from SUB_QQ_Q import SUB_QQ_Q
#Функции не из списка
from MUL_ZM_Z import MUL_ZM_Z


def SUB_PP_P(a: cls.polynom, b: cls.polynom):
    f = deepcopy(a)
    g = deepcopy(b)

    f.coef.reverse()
    g.coef.reverse()

    new_coef = []

    for i, x in enumerate(g.coef):
        if i > f.deg:
            x.numerator = MUL_ZM_Z(x.numerator)
            new_coef.append(x)
        else:
            new_coef.append(SUB_QQ_Q(f.coef[i], x))

    new_coef.reverse()

    return cls.polynom(new_coef)