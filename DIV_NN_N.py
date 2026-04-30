"""
N-11
Неполное частное от деления первого натурального числа на второе с остатком (делитель отличен от нуля)
DIV_NN_N
"""

from copy import deepcopy
import classes as cl
from COM_NN_D import COM_NN_D
from ADD_NN_N import ADD_NN_N
from DIV_NN_Dk import DIV_NN_Dk
from SUB_NN_N import SUB_NN_N
from MUL_NN_N import MUL_NN_N

def DIV_NN_N(a_arg : cl.natural, b_arg : cl.natural):
    a = deepcopy(a_arg)
    b = deepcopy(b_arg)
    rest = a
    sum = cl.natural([0])
    while(COM_NN_D(rest, b) != 1):
        shift = DIV_NN_Dk(rest, b)
        sum = ADD_NN_N(sum, shift)
        rest = SUB_NN_N(rest, MUL_NN_N(b, shift))
    return sum