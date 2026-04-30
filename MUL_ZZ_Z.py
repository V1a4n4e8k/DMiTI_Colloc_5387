"""
Z-8
Умножение целых чисел
"""


from copy import deepcopy

import classes as cls

#from SGN_Z_D import SGN_Z_D
#from ABS_Z_Z import ABS_Z_Z
from MUL_NN_N import MUL_NN_N
from NZER_N_B import NZER_N_B
#from MUL_ZM_Z import MUL_ZM_Z


def MUL_ZZ_Z(a: cls.integer, b: cls.integer):
    if (NZER_N_B(a.data) == 0 or NZER_N_B(b.data) == 0):
        return cls.integer(0, cls.natural([0]))

    f = deepcopy(a)
    g = deepcopy(b)
    
    new_data = MUL_NN_N(f.data, g.data)

    if f.sign == g.sign:
        new_sign = 0
    else:
        new_sign = 1
    
    output = cls.integer(new_sign, new_data)

    return output