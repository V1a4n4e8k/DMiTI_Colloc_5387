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
    res = cl.polynom([cl.rational(cl.integer(0,cl.natural([0])),cl.natural([1]))])
    count = a.deg
    while(count >= 0):
        add = MUL_PQ_P(b, a.coef[count])
        add = MUL_Pxk_P(add, count)
        res = ADD_PP_P(res, add)
        count -= 1
    return res