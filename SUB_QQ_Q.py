"""
Q-6
Вычитание дробей
"""


from copy import deepcopy

import classes as cls

from LCM_NN_N import LCM_NN_N
from MUL_ZZ_Z import MUL_ZZ_Z
from SUB_ZZ_Z import SUB_ZZ_Z
#Функции не из списка
from DIV_NN_N import DIV_NN_N


def SUB_QQ_Q(a: cls.rational, b: cls.rational):
    f = deepcopy(a)
    g = deepcopy(b)

    lcm = LCM_NN_N(f.denominator, g.denominator)

    f_c = DIV_NN_N(lcm, f.denominator)
    g_c = DIV_NN_N(lcm, g.denominator)

    new_f_num = MUL_ZZ_Z(f.numerator, cls.integer(0, f_c))
    new_g_num = MUL_ZZ_Z(g.numerator, cls.integer(0, g_c))

    sub = SUB_ZZ_Z(new_f_num, new_g_num)

    output = cls.rational(sub, lcm)

    return output