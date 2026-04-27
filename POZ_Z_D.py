"""
Z-2
Определение положительности числа (2 - положительное, 0 — равное нулю, 1 - отрицательное)
Предложили заменить на более стандартное обозначение и вывод как
"""

import classes

def POZ_Z_D(a: classes.integer):
    if a.data.n == 1 and a.data.data[0] == 0:
        return 0

    if a.sign == 0:
        return 2

    return 1