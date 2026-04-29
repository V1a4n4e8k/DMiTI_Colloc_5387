"""
N-5
Вычитание из первого большего натурального числа второго меньшего или равного
"""

from COM_NN_D import COM_NN_D
import classes
from classes import natural


def SUB_NN_N(a : classes.natural, b : classes.natural):
    # по условию a >= b
    if COM_NN_D(a, b) == 1:
        return None

    res = a.data.copy()  # чтобы не портить исходный массив

    i = len(res) - 1
    j = b.n - 1

    while i >= 0:
        tmp_b = b.data[j] if j >= 0 else 0
        if res[i] >= tmp_b:
            res[i] -= tmp_b
        else:
            res[i - 1] -= 1
            res[i] = res[i] + 10 - tmp_b

        i -= 1
        j -= 1

    # убираем ведущие нули, но оставляем один ноль
    while len(res) > 1 and res[0] == 0:
        res.pop(0)

    return classes.natural(res)
