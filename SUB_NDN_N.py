"""
N-9
Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом
SUB_NDN_N <- SUB_NN_N; MUL_ND_N; COM_NN_D
"""
from copy import deepcopy
import classes as cl
from SUB_NN_N import SUB_NN_N
from MUL_ND_N import MUL_ND_N
from COM_NN_D import COM_NN_D

def SUB_NDN_N(a : cl.natural, b : cl.natural, c : int):
    b_new = deepcopy(b)
    b_new = MUL_ND_N(b_new, c)
    if COM_NN_D(a, b_new) == 1:
        return None
    return SUB_NN_N(a, b_new)
