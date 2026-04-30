"""
Z-10
Остаток от деления целого на целое(делитель отличен от нуля)
"""


from copy import deepcopy

import classes as cls

from DIV_ZZ_Z import DIV_ZZ_Z
from MUL_ZZ_Z import MUL_ZZ_Z
from SUB_ZZ_Z import SUB_ZZ_Z

def MOD_ZZ_Z(a: cls.integer, b: cls.integer):
    f = deepcopy(a)
    g = deepcopy(b)
    
    div = DIV_ZZ_Z(f, g)

    div = MUL_ZZ_Z(div, g)

    output = SUB_ZZ_Z(f, div)

    return output