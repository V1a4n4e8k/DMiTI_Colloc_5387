"""
N-5
Вычитание из первого большего натурального числа второго меньшего или равного
"""

from COM_NN_D import COM_NN_D

def SUB_NN_N(a, b):
    # по условию a >= b
    if COM_NN_D(a, b) == 1:
        return None

    a = a[:]  # чтобы не портить исходный массив

    i = len(a) - 1
    j = len(b) - 1

    while j >= 0:
        if a[i] >= b[j]:
            a[i] -= b[j]
        else:
            a[i - 1] -= 1
            a[i] = a[i] + 10 - b[j]

        i -= 1
        j -= 1

    # убираем ведущие нули, но оставляем один ноль
    while len(a) > 1 and a[0] == 0:
        a.pop(0)

    return a

""" ПРИМЕР ИСПОЛЬЗОВАНИЯ
a = [1,2,3,4]
b = [3,4,5]
SUB_NN_N(a,b)

print(print(a))
"""
a = [1,2,3,4]
b = [3,4,5]
c = SUB_NN_N(a,b)

print(c)