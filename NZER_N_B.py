"""
N-2
Проверка на ноль: если число не равно нулю, то «да» иначе «нет»
"""

import classes

def NZER_N_B(a: classes.natural):
    if a.n == 1 and a.data[0] == 0:
        return 0
    return 1
