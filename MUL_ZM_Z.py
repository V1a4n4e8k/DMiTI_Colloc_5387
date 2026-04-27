"""
Z-3
Умножение целого на (-1)
"""

import classes

def MUL_ZM_Z(a: classes.integer):
    output = classes.integer(a.sign, classes.natural(a.data.data))

    # меняем знак
    if(a.sign == 1):
        output.sign = 0
    elif(a.sign == 0):
        output.sign = 1

    return output


#Функция умножения целого числа на -1:

#Функция возвращает новое целое число, знак которого противоположен знаку аргумента

#Аргумент функции не меняется и не связывается