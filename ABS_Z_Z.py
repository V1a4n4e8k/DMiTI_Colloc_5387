"""
Z-1
Абсолютная величина числа, результат - целое
"""


from copy import deepcopy

import classes as cls


def ABS_Z_Z(a: cls.integer):
    output = deepcopy(a)
    
    output.sign = 0
    
    return output