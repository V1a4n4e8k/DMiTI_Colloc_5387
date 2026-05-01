"""
Q-7
Умножение дробей
"""


from copy import deepcopy

import classes as cls

from MUL_ZZ_Z import MUL_ZZ_Z
#Функции не из списка
from MUL_NN_N import MUL_NN_N


def MUL_QQ_Q(a: cls.rational, b: cls.rational):
    f = deepcopy(a)
    g = deepcopy(b)
    
    new_num = MUL_ZZ_Z(f.numerator, g.numerator)
    new_den = MUL_NN_N(f.denominator, g.denominator)

    output = cls.rational(new_num, new_den)

    return output