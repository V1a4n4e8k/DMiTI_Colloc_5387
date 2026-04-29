"""
Z-8
Умножение целых чисел
"""


from copy import deepcopy

import classes as cls

#from SGN_Z_D import SGN_Z_D
#from ABS_Z_Z import ABS_Z_Z
from MUL_NN_N import MUL_NN_N
#from MUL_ZM_Z import MUL_ZM_Z


def MUL_ZZ_Z(a: cls.integer, b: cls.integer):
    f = deepcopy(a)
    g = deepcopy(b)
    
    new_data = MUL_NN_N(f.data, g.data)

    if f.sign == g.sign:
        new_sign = 0
    else:
        new_sign = 1
    
    output = cls.integer(new_sign, new_data)

    return output