"""
Z-7
Вычитание целых чисел
"""


from copy import deepcopy

import classes as cls

#from SGN_Z_D import SGN_Z_D
#from ABS_Z_Z import ABS_Z_Z
from COM_NN_D import COM_NN_D
from ADD_NN_N import ADD_NN_N
from SUB_NN_N import SUB_NN_N
from MUL_ZM_Z import MUL_ZM_Z


def SUB_ZZ_Z(a: cls.integer, b: cls.integer):
    f = deepcopy(a)
    g = deepcopy(b)

    #Умножаем вычитаемое на (-1)
    g = MUL_ZM_Z(g)

    cmp = COM_NN_D(f.data, g.data)

    if cmp == 2:
        big = f
        sml = g
    elif cmp == 1:
        big = g
        sml = f
    elif cmp == 0:
        #Без разницы, какое значение больше
        big = f
        sml = g
    
    if f.sign == g.sign:
        new_data = ADD_NN_N(f.data, g.data)
        new_sign = f.sign
    else:
        new_data = SUB_NN_N(big.data, sml.data)
        new_sign = big.sign
    
    output = cls.integer(new_sign, new_data)

    return output