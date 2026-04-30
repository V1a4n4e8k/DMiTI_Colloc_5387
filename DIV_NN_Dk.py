"""
N-10
DIV_NN_Dk
Вычисление первой цифры деления большего натурального на меньшее, домноженное на 10^k,
где k - номер позиции этой цифры (номер считается с нуля)
"""
from copy import deepcopy
import classes as cl
from COM_NN_D import COM_NN_D
from MUL_Nk_N import MUL_Nk_N
from MUL_ND_N import MUL_ND_N

def DIV_NN_Dk(a_arg: cl.natural, b_arg: cl.natural):
    if b_arg.n == 1 and b_arg.data[0] == 0:
        return None

    if COM_NN_D(a_arg, b_arg) == 1:
        return None

    a = deepcopy(a_arg)
    b = deepcopy(b_arg)
    n1 = a.n
    n2 = b.n
    k = n1 - n2
    b_cmp = MUL_Nk_N(b, k)
    if COM_NN_D(a, b_cmp) == 1:
        k -= 1
    for dig in range(9, 0, -1):
        b_tmp = MUL_ND_N(b, dig)
        cmp = MUL_Nk_N(b_tmp, k)
        if COM_NN_D(cmp, a) != 2:
            out = cl.natural([dig])
            return MUL_Nk_N(out, k)
    return cl.natural([0])
