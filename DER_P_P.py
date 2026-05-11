"""
P-12
Производная многочлена
"""

from copy import deepcopy
import classes as cl

from MUL_QQ_Q import MUL_QQ_Q


def DER_P_P(p: cl.polynom):
    poly = deepcopy(p)

    # производная от константы = 0
    if poly.deg == 0:
        return cl.polynom([
            cl.rational(
                cl.integer(0, cl.natural([0])),
                cl.natural([1])
            )
        ])

    new_coef = []

    # умножаем показатель степени на коэффициент при его члене
    for i in range(len(poly.coef) - 1):
        pow = poly.deg - i

        pow_q = cl.rational(
            cl.integer(0, cl.natural(list(map(int, str(pow))))),
            cl.natural([1])
        )

        new_coef.append(MUL_QQ_Q(poly.coef[i], pow_q))

    return cl.polynom(new_coef)