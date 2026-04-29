"""
Z-4
Преобразование натурального в целое
"""


import classes as cls


def TRANS_N_Z(a: cls.natural):
    output = cls.integer(0, cls.natural(a.data))
    return output