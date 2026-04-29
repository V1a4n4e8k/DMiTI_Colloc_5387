"""
Z-5
Преобразование целого неотрицательного в натуральное
"""


from copy import deepcopy

import classes as cls


def TRANS_Z_N(a: classes.integer):
    output = deepcopy(a)
    return output.data