"""
N-13
НОД натуральных чисел
GCF_NN_N
"""
from copy import deepcopy
import classes as cl
from NZER_N_B import NZER_N_B
from MOD_NN_N import MOD_NN_N

def GCF_NN_N(a_arg : cl.natural, b_arg : cl.natural):
    a = deepcopy(a_arg)
    b = deepcopy(b_arg)
    while(NZER_N_B(b) == 1):
        ost = MOD_NN_N(a, b)
        a = b
        b = ost
    return a