"""
Z-2
Определение положительности числа (1 - положительное, 0 — равное нулю, -1 - отрицательное)
"""


import classes as cls


def SGN_Z_D(a: cls.integer):
    if a.data.n == 1 and a.data.data[0] == 0:
        return 0 
    
    if a.sign == 1:
        return -1
    
    return 1