"""
N-12
Остаток от деления первого натурального числа на второе натуральное (делитель отличен от нуля)
MOD_NN_N
"""

from copy import deepcopy
import classes as cl
from DIV_NN_N import DIV_NN_N
from SUB_NN_N import SUB_NN_N
from MUL_NN_N import MUL_NN_N

def MOD_NN_N(a_arg : cl.natural, b_arg : cl.natural):
    a = deepcopy(a_arg)
    b = deepcopy(b_arg)
    div = DIV_NN_N(a, b)
    return SUB_NN_N(a, MUL_NN_N(div, b))
