"""
Z-9
Частное от деления целого на целое (делитель отличен от нуля)
"""

from copy import deepcopy

import classes as cls

from DIV_NN_N import DIV_NN_N
from MOD_NN_N import MOD_NN_N
from ADD_1N_N import ADD_1N_N
from NZER_N_B import NZER_N_B


def DIV_ZZ_Z(a: cls.integer, b: cls.integer):
    f = deepcopy(a)
    g = deepcopy(b)

    if NZER_N_B(g.data) == 0:
        return None

    q = DIV_NN_N(f.data, g.data)
    r = MOD_NN_N(f.data, g.data)

    if f.sign == 1 and NZER_N_B(r) == 1:
        q = ADD_1N_N(q)

    if f.sign == g.sign:
        new_sign = 0
    else:
        new_sign = 1

    if NZER_N_B(q) == 0:
        new_sign = 0

    return cls.integer(new_sign, q)
