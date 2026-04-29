"""
N-1
Сравнение натуральных чисел: 2 - если первое больше второго, 0, если равно, 1 иначе.
"""

import classes

def COM_NN_D(a: classes.natural, b: classes.natural):
    if a.n > b.n:
        return 2
    if a.n < b.n:
        return 1

    for i in range(a.n):
        if a.data[i] > b.data[i]:
            return 2
        if a.data[i] < b.data[i]:
            return 1

    return 0

