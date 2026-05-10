"""
P-8
Умножение многочленов
MUL_PP_P
"""
from copy import deepcopy
import classes as cl
from MUL_PQ_P import MUL_PQ_P
from MUL_Pxk_P import MUL_Pxk_P
from ADD_PP_P import ADD_PP_P

def MUL_PP_P(a_arg: cl.polynom, b_arg: cl.polynom):
    a = deepcopy(a_arg)
    b = deepcopy(b_arg)

    zero = cl.rational(
        cl.integer(0, cl.natural([0])),
        cl.natural([1])
    )

    res = cl.polynom([zero])

    for i in range(len(a.coef)):
        pow = a.deg - i

        add = MUL_PQ_P(b, a.coef[i])
        add = MUL_Pxk_P(add, pow)

        res = ADD_PP_P(res, add)

    return res