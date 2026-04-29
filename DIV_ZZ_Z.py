"""
Z-9
Частное от деления целого на целое (делитель отличен от нуля)
"""


from copy import deepcopy

import classes as cls

#from ABS_Z_Z import ABS_Z_Z
#from SGN_Z_D import SGN_Z_D
from DIV_NN_N import DIV_NN_N
#from ADD_1N_N import ADD_1N_N


def DIV_ZZ_Z(a: cls.integer, b: cls.integer):
    f = deepcopy(a)
    g = deepcopy(b)
    
    new_data = DIV_NN_N(f.data, g.data)

    if f.sign == g.sign:
        new_sign = 0
    else:
        new_sign = 1
    
    output = cls.integer(new_sign, new_data)

    return output