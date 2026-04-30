"""
N-14
НОК натуральных чисел
LCM_NN_N
"""

from copy import deepcopy
import classes as cl
from MUL_NN_N import MUL_NN_N
from DIV_NN_N import DIV_NN_N
from GCF_NN_N import GCF_NN_N

def LCM_NN_N(a_arg: cl.natural, b_arg: cl.natural):
    a = deepcopy(a_arg)
    b = deepcopy(b_arg)
    return DIV_NN_N(MUL_NN_N(a, b), GCF_NN_N(a, b))