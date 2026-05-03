"""
Q-8
Деление дробей
"""


from copy import deepcopy

import classes as cls

from MUL_ZZ_Z import MUL_ZZ_Z
#Функции не из списка
from MUL_NN_N import MUL_NN_N
from NZER_N_B import NZER_N_B
from RED_Q_Q import RED_Q_Q


def DIV_QQ_Q(a: cls.rational, b: cls.rational):
    f = deepcopy(a)
    g = deepcopy(b)
    
    if NZER_N_B(g.numerator.data) == 0:
        return None

    new_num = MUL_ZZ_Z(f.numerator, cls.integer(g.numerator.sign, g.denominator))
    new_den = MUL_NN_N(f.denominator, g.numerator.data)

    output = RED_Q_Q(cls.rational(new_num, new_den))

    return output