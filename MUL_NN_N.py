"""
N-8
Умножение натуральных чисел
"""

import classes
import MUL_ND_N
import MUL_Nk_N
import ADD_NN_N

def MUL_NN_N(a: classes.natural, b: classes.natural):
    # если одно из чисел = 0
    if (a.n == 1 and a.data[0] == 0) or (b.n == 1 and b.data[0] == 0):
        return classes.natural([0])

    result = classes.natural([0])

    k = 0
    j = b.n - 1

    while j >= 0:
        # умножаем a на одну цифру b
        part = MUL_ND_N.MUL_ND_N(a, b.data[j])

        # домножаем на 10^k тк у нас сдвиги при умножении в столбик
        part = MUL_Nk_N.MUL_Nk_N(part, k)

        # прибавляем к результату
        result = ADD_NN_N.ADD_NN_N(result, part)

        k += 1
        j -= 1

    return result