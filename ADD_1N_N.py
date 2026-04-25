"""
N-3
Добавление 1 к натуральному числу
"""

def ADD_1N_N(a):
    i = len(a) - 1

    while i >= 0:
        if a[i] != 9:
            a[i] += 1
            return a
        else:
            a[i] = 0
            i -= 1

    # если все цифры были 9
    return [1] + a

""" use ex
a = [1][9]
print(ADD_1N_N(a))
"""
