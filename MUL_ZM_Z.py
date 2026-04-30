"""
Z-3
Умножение целого на (-1)
"""


from copy import deepcopy
from NZER_N_B import NZER_N_B
import classes as cls


def MUL_ZM_Z(a: cls.integer):
    if NZER_N_B(a.data) == 0:
        return a

    output = deepcopy(a)

    if (a.sign == 1):
        output.sign = 0
    elif (a.sign == 0):
        output.sign = 1

    return output