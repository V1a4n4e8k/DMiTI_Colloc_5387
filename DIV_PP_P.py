"""
P-9
Частное от деления многочлена на многочлен при делении с остатком
"""

from copy import deepcopy
import classes as cl

from SUB_PP_P import SUB_PP_P
from MUL_PQ_P import MUL_PQ_P
from MUL_Pxk_P import MUL_Pxk_P
from ADD_PP_P import ADD_PP_P
from DIV_QQ_Q import DIV_QQ_Q


def zero_q():
    return cl.rational(
        cl.integer(0, cl.natural([0])),
        cl.natural([1])
    )


def zero_p():
    return cl.polynom([zero_q()])


def is_zero_poly(p: cl.polynom):
    return (
        p.deg == 0
        and p.coef[0].numerator.data.n == 1
        and p.coef[0].numerator.data.data[0] == 0
    )


def DIV_PP_P(a_arg: cl.polynom, b_arg: cl.polynom):
    a = deepcopy(a_arg)
    b = deepcopy(b_arg)

    if is_zero_poly(b):
        return None

    if a.deg < b.deg:
        return zero_p()

    result = zero_p()

    # реализация столбика
    while a.deg >= b.deg and not is_zero_poly(a):
        pow = a.deg - b.deg

        coef = DIV_QQ_Q(a.coef[0], b.coef[0])

        # копим частное
        tmp = cl.polynom([coef])
        tmp = MUL_Pxk_P(tmp, pow)

        result = ADD_PP_P(result, tmp)

        sub_part = MUL_PQ_P(b, coef)
        sub_part = MUL_Pxk_P(sub_part, pow)

        a = SUB_PP_P(a, sub_part)

    return result