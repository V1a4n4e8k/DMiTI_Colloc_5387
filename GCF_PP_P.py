"""
P-11
НОД многочленов
GCF_PP_P
"""

from copy import deepcopy
import classes as cl

from MOD_PP_P import MOD_PP_P
from MUL_PQ_P import MUL_PQ_P
from DIV_QQ_Q import DIV_QQ_Q


def zero_q():
    return cl.rational(
        cl.integer(0, cl.natural([0])),
        cl.natural([1])
    )


def one_q():
    return cl.rational(
        cl.integer(0, cl.natural([1])),
        cl.natural([1])
    )


def is_zero_poly(p: cl.polynom):
    return (
        p.deg == 0
        and p.coef[0].numerator.data.n == 1
        and p.coef[0].numerator.data.data[0] == 0
    )


def GCF_PP_P(a_arg: cl.polynom, b_arg: cl.polynom):
    a = deepcopy(a_arg)
    b = deepcopy(b_arg)

    # Алгоритм Евклида
    while not is_zero_poly(b):
        ost = MOD_PP_P(a, b)
        a = b
        b = ost

    if is_zero_poly(a):
        return a

    # делаем НОД так чтобы старший коэффициент был положительным
    st = a.coef[0]
    factor = DIV_QQ_Q(one_q(), st)

    return MUL_PQ_P(a, factor)