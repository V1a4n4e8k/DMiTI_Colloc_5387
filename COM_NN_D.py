"""
N-1
Сравнение натуральных чисел: 2 - если первое больше второго, 0, если равно, 1 иначе.
"""

def COM_NN_D(a, b):
    # Сравнение длины
    if len(a) > len(b):
        return 2
    if len(a) < len(b):
        return 1

    # Поразрядное сравнение
    for i in range(len(a)):
        if a[i] > b[i]:
            return 2
        if a[i] < b[i]:
            return 1

    # Равны
    return 0

""" use ex
print(COM_NN_D([3,2,3,4],[2,3,4]))
"""
print(COM_NN_D([3,2,3,4],[2,3,4]))